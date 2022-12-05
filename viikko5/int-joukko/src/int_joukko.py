""" 
- Poista copypaste
- Vähennä monimutkaisuutta
- Anna muuttujille selkeät nimet
- Tee metodeista pienempiä ja hyvän koheesion omaavia 
"""

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.ljono = []

    def kuuluu(self, luku):
        if luku in self.ljono:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono.append(luku)

    def poista(self, luku):
        self.ljono.remove(luku)

    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        return self.ljono

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            yhdiste.lisaa(luku)
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for luku in a.to_int_list():
            if b.kuuluu(luku):
                leikkaus.lisaa(luku)
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                erotus.lisaa(luku)
        return erotus

    def __str__(self):
        return "{" + str(self.ljono)[1:-1] + "}"
