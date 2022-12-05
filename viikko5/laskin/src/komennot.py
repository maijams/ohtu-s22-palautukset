class Komento:
    def __init__(self, sovelluslogiikka, syote):
        self.sovellus = sovelluslogiikka
        self.syote = syote
        self.edellinen = 0

    def kumoa(self):
        self.sovellus.kumoa(self.edellinen)


class Summa(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.hae_tulos()
        self.sovellus.plus(self.syote())
        

class Erotus(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.hae_tulos()
        self.sovellus.miinus(self.syote())


class Nollaus(Komento):
    def suorita(self):
        self.edellinen = self.sovellus.hae_tulos()
        self.sovellus.nollaa()

        
class Kumoa(Komento):
    def suorita(self):
        pass

