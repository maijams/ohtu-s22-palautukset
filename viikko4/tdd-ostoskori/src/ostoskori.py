from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.sisalto = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        maara = 0
        for ostos in self.sisalto:
            maara += ostos.lukumaara()
        return maara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        summa = 0
        for ostos in self.sisalto:
            summa += ostos.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        korissa = False
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                korissa = True
                ostos.muuta_lukumaaraa(1)
        if not korissa:
            self.sisalto.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        # tyhjentää ostoskorin
        pass

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.sisalto    