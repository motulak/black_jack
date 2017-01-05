import random

''': spades (♠), hearts (♥), diamonds (♦) and clubs (♣)'''

class Gra(object):
    def __init__(self, lista_graczy):
        self.czy_grac = True
        self.runda = 0
        print '''Witamy w naszej grze:'''
        self.talia = Talia()
        self.kasyno = Kasyno()
        self.krupier = Gracz('Krupier')
        self.kasyno.dodaj_gracza(self.krupier)
        for gracz in lista_graczy:
            self.gracz = Gracz(gracz)
            self.kasyno.dodaj_gracza(self.gracz)

        while self.czy_grac == True:
            if self.kasyno.jest_black_jack() == True:
                self.czy_grac = False
                print "Jest Black Jack - KONIEC GRY"
            else:
                self.kasyno.wyrzuc_przegranych_graczy()
                if self.kasyno.czy_ktos_jest_w_grze() == False:
                    self.czy_grac = False
                    print "Wszyscy odpadli - KONIEC GRY"
                else:
                    print ""
                    print "Runda", self.runda
                    if self.runda == 0:
                        self.talia.rozdaj(self.kasyno.gracze, 2)
                    else:
                        self.talia.rozdaj(self.kasyno.gracze, 1)

                    self.kasyno.wysywietl_obecny_stan()
                    self.runda += 1


class Kasyno(object):

    def __init__(self):
        self.gracze = []
        self.przegrani = []


    def oblicz_reke(self,reka):
        wartosc_reki = 0
        for karta in reka.karty:
            if karta.figura not in ('J','Q','K','A'):
                wartosc_obecnej_karty = int(karta.figura)
            if karta.figura in ('J','Q','K'):
                wartosc_obecnej_karty = 10
            if karta.figura == 'A':
                wartosc_obecnej_karty = 11
            wartosc_reki += wartosc_obecnej_karty
        if wartosc_reki > 21:
            for karta in reka.karty:
                if karta.figura == 'A' and wartosc_reki>21:
                    wartosc_reki -= 10
        return wartosc_reki


    def dodaj_gracza(self,gracz):
        self.gracze.append(gracz)


    def jest_black_jack(self):
        for gracz in self.gracze:
            if self.oblicz_reke(gracz) == 21:
                return True
        if self.gracze.__len__()==0:
            return True
        else:
            return False



    def wyrzuc_przegranych_graczy(self):
        for x in self.gracze:
            wartosc = self.oblicz_reke(x)
            if wartosc > 21 and x.rozdawac==True :
                x.nie_rozdawaj_kart()
                print " {:<5} - odpada".format(x.imie)






    def wysywietl_obecny_stan(self):
        for gracz in self.gracze:
            if gracz.rozdawac == True:
                print "{:<10} ".format(gracz.imie),
                print gracz, "  =  ",
                print str(self.oblicz_reke(gracz))








    def czy_ktos_jest_w_grze(self):
        for x in self.gracze:
            if x.rozdawac == True:
                return True
            else:
                return False




class Karta(object):

    def __init__(self, figura, kolor):
        self.figura = figura
        self.kolor = kolor

    def __str__(self):
        return str("|{:>3} {:<6}| ".format(self.figura,self.kolor))

class Gracz(object):

    def __init__(self,imie):
        self.karty = []
        self.imie = imie
        self.rozdawac = True

    def nie_rozdawaj_kart(self):
        self.rozdawac = False

    def rozdawaj_karty(self):
        self.rozdawac = True


    def dodaj(self,karta):
        self.karty.append(karta)

    def oddaj(self,karta,reka):
        self.karty.remove(karta)
        reka.dodaj(karta)

    def __str__(self):
        text = ''
        if self.karty:
            for karta in self.karty:
                text += str(karta)
        else:
            text = '<reka pusta>'
        return text


class Talia(Gracz):
    kolory = ['pik','kier','trefl','karo']
    figury = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def __init__(self):
        self.karty = []
        self.nowa()
        self.tasuj()

    def nowa(self):
        for kolor in self.kolory:
            for figura in self.figury:
                karta = Karta(figura,kolor)
                self.dodaj(karta)


    def tasuj(self):
        random.shuffle(self.karty)

    def rozdaj(self,osoby,ile_kart):
        for kolejka in range(ile_kart):
            for reka in osoby:
                if reka.rozdawac == True:
                    self.oddaj(self.karty[0],reka)


    def listuj(self):
        i=0
        text = ''
        if self.karty:
            for karta in self.karty:
                i +=1
                text += str(karta)
                if i%13 == 0 :
                    text += '\n'


        else:
            text = '<reka pusta>'
        print text





if __name__ == '__main__':
    print "mama ne"