class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos


class Summa:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka
        self.syote = 0

    def suorita(self):
        self.sovellus.tulos += self.syote


class Erotus:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka
        self.syote = 0

    def suorita(self):
        self.sovellus.tulos -= self.syote
 

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka

    def suorita(self):
        self.sovellus.tulos = 0

        
class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovellus = sovelluslogiikka
        self.syote = 0

    def suorita(self):
        pass

