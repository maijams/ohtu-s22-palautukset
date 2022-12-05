class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        
    def plus(self, luku):
        self.tulos += luku
    
    def miinus(self, luku):
        self.tulos -= luku
    
    def nollaa(self):
        self.tulos = 0
        
    def kumoa(self, luku):
        self.tulos = luku
        
    def hae_tulos(self):
        return self.tulos
        
    

