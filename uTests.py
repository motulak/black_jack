import unittest
from cards import *


class TestCards(unittest.TestCase):
    def test_check(self):
        self.assertEqual('foo'.upper(), 'FOO')
        #self.fail('Oops')

    def test_Karta(self):
        x = Karta('2','pik')
        t = str(x)
        self.assertEqual(t, '|  2 pik   | ')


    def test_Reka_inicjalizacja(self):
        reka = Gracz('X')
        output1 = str(reka)
        self.assertEqual(output1, '<reka pusta>')


    def test_Reka_dodaj_karty(self):
        reka = Gracz('Z')
        karta1 = Karta('2','pik')
        karta2 = Karta('A', 'karo')
        reka.dodaj(karta1)
        output1 = str(reka)
        self.assertEqual(output1,'|  2 pik   | ')
        reka.dodaj(karta2)
        output1 = str(reka)
        self.assertEqual(output1,'|  2 pik   | |  A karo  | ')


    def test_Reka_oddaj_karte(self):
        reka1=Gracz('X')
        reka2=Gracz('Y')
        karta1=Karta('2','kier')
        reka1.dodaj(karta1)
        reka1.oddaj(karta1,reka2)
        output1 = str(reka2)
        self.assertEqual(output1,'|  2 kier  | ')
        output1 = str(reka1)
        self.assertEqual(output1,'<reka pusta>')


    def liczenie_2_kart(self,akarta,bkarta,ilepowinnobyc):
        reka1 = Gracz('Adam')
        karta1=Karta(akarta,'kier')
        karta2=Karta(bkarta,'pik')
        reka1.dodaj(karta1)
        reka1.dodaj(karta2)
        kasyno = Kasyno()
        x = kasyno.oblicz_reke(reka1)
        self.assertEqual(x,ilepowinnobyc)

    def liczenie_3_kart(self, akarta, bkarta,ckarta, ilepowinnobyc):
        reka1 = Gracz('Adam')
        karta1 = Karta(akarta, 'kier')
        karta2 = Karta(bkarta, 'pik')
        karta3 = Karta(ckarta, 'pik')
        reka1.dodaj(karta1)
        reka1.dodaj(karta2)
        reka1.dodaj(karta3)
        kasyno = Kasyno()
        x = kasyno.oblicz_reke(reka1)
        self.assertEqual(x, ilepowinnobyc)

    def test_liczenia_kart(self):
        self.liczenie_2_kart('1', '2', 3)
        self.liczenie_2_kart('1', '3', 4)
        self.liczenie_2_kart('9', '9', 18)
        self.liczenie_2_kart('10', '10', 20)
        self.liczenie_2_kart('1', 'J', 11)
        self.liczenie_2_kart('10', 'Q', 20)
        self.liczenie_2_kart('10', 'K', 20)
        self.liczenie_2_kart('1', 'A', 12)
        self.liczenie_2_kart('Q', 'A', 21)
        self.liczenie_2_kart('A', 'A', 12)
        self.liczenie_3_kart('1', '1', '1', 3)
        self.liczenie_3_kart('Q', 'Q', '10', 30)
        self.liczenie_3_kart('A', '1', '1', 13)
        self.liczenie_3_kart('A', '10', 'Q', 21)
        self.liczenie_3_kart('A', 'A', '1', 13)
        self.liczenie_3_kart('A', 'A', 'A', 13)
        self.liczenie_3_kart('2', 'A', 'K', 13)
        self.liczenie_3_kart('2', 'A', 'Q', 13)
        self.liczenie_3_kart('2', 'A', 'J', 13)


    def dodaj_reke_i_karty(self, reka, akarta, bkarta):
        karta1 = Karta(akarta, 'kier')
        karta2 = Karta(bkarta, 'pik')
        reka.dodaj(karta1)
        reka.dodaj(karta2)
        return reka


    def dodaj_3_graczy(self):
        reka1 = Gracz('Adam')
        reka2 = Gracz('Wojtek')
        reka3 = Gracz('Ziutek')
        self.dodaj_reke_i_karty(reka1,'1','2')
        self.dodaj_reke_i_karty(reka2,'A','Q')
        self.dodaj_reke_i_karty(reka3,'A','A')
        kasyno = Kasyno()
        kasyno.dodaj_gracza(reka1)
        kasyno.dodaj_gracza(reka2)
        kasyno.dodaj_gracza(reka3)


    def test_wyswietlania_graczy(self):
        reka1 = Gracz('Adam')
        reka2 = Gracz('Wojtek')
        reka3 = Gracz('Ziutek')
        self.dodaj_reke_i_karty(reka1,'1','2')
        self.dodaj_reke_i_karty(reka2,'A','Q')
        self.dodaj_reke_i_karty(reka3,'A','A')
        kasyno = Kasyno()
        kasyno.dodaj_gracza(reka1)
        kasyno.dodaj_gracza(reka2)
        kasyno.dodaj_gracza(reka3)
        kasyno.wysywietl_obecny_stan()


    def test_rozdanie(self):
        kasyno = Kasyno()
        gracz1 = Gracz('Adam')
        gracz2 = Gracz('Basia')
        gracz3 = Gracz('Cecylia')
        kasyno.dodaj_gracza(gracz1)
        kasyno.dodaj_gracza(gracz2)
        kasyno.dodaj_gracza(gracz3)
        nowa_talia = Talia()
        nowa_talia.nowa()
        nowa_talia.tasuj()
        nowa_talia.rozdaj(kasyno.gracze,1)
        kasyno.wysywietl_obecny_stan()
        nowa_talia.rozdaj(kasyno.gracze, 1)
        kasyno.wysywietl_obecny_stan()
        nowa_talia.rozdaj(kasyno.gracze, 1)
        kasyno.wysywietl_obecny_stan()
        nowa_talia.rozdaj(kasyno.gracze, 1)
        kasyno.wysywietl_obecny_stan()
        print kasyno.jest_black_jack()

    def testuj_gra(self):
        gracze = ('Zenek','Rysio','Xawier')
        gra = Gra(gracze)


if __name__ == '__main__':
    unittest.main()
