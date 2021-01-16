# Project UAS PBO Teori
# Nama      : Nadhif Hakiim Risantosa
# NIM       : 081911633070
# Hari, Tgl : Jum'at, 17 Januari 2021

# parent class yakni object "MataUang"
class MataUang:
    
    # konstruktor dengan parameter overloading (memiliki nilai default)
    def __init__(self, negara:str = "Indonesia", amount:int = 0):
        self.negara = negara
        self.amount = amount
    
    # method untuk print object
    def toString(self):
        pass