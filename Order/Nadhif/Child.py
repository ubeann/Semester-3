# Project UAS PBO Teori
# Nama      : Nadhif Hakiim Risantosa
# NIM       : 081911633070
# Hari, Tgl : Jum'at, 17 Januari 2021

from Parent import MataUang     # import parent class

# Set mata uang
import locale
locale.setlocale(locale.LC_ALL, '')

# variable control
textKode:str   = "Kode ID  :"
textNama:str   = "Mata Uang:"
textNegara:str = "Negara   :"
textAmount:str = "Jumlah   :"

# merupakan child class dengan parent class "MataUang"
class Rupiah(MataUang):
    # konstruktor dengan parameter overloading (memiliki nilai default)
    # serta overriding dengan parent
    def __init__(self, negara:str = "Indonesia", amount:int = 0):
        super().__init__(negara, amount)
        self.kode:str   = "IDR"
        self.simbol:str = "Rp."
        self.nama:str   = "Rupiah"
    
    # method untuk print object (overriding dengan parent)
    def toString(self):
        print(textKode, self.kode)
        print(textNama, self.nama)
        print(textNegara, self.negara)
        print(textAmount, self.simbol, locale.currency( self.amount, symbol=False, grouping=True ))

class DollarUS(MataUang):
    # konstruktor dengan parameter overloading (memiliki nilai default)
    # serta overriding dengan parent
    def __init__(self, negara:str = "Amerika", amount:int = 0):
        super().__init__(negara, amount)
        self.kode:str   = "USD"
        self.simbol:str = "$"
        self.nama:str   = "DollarUS"
    
    # method untuk print object (overriding dengan parent)
    def toString(self):
        print(textKode, self.kode)
        print(textNama, self.nama)
        print(textNegara, self.negara)
        print(textAmount, self.simbol, locale.currency( self.amount, symbol=False, grouping=True ))

class Yuan(MataUang):
    # konstruktor dengan parameter overloading (memiliki nilai default)
    # serta overriding dengan parent
    def __init__(self, negara:str = "China", amount:int = 0):
        super().__init__(negara, amount)
        self.kode:str   = "CNY"
        self.simbol:str = "CNY"
        self.nama:str   = "Yuan"
    
    # method untuk print object (overriding dengan parent)
    def toString(self):
        print(textKode, self.kode)
        print(textNama, self.nama)
        print(textNegara, self.negara)
        print(textAmount, self.simbol, locale.currency( self.amount, symbol=False, grouping=True ))

class Euro(MataUang):
    # konstruktor dengan parameter overloading (memiliki nilai default)
    # serta overriding dengan parent
    def __init__(self, negara:str = "Uni Eropa", amount:int = 0):
        super().__init__(negara, amount)
        self.kode:str   = "EUR"
        self.simbol:str = "EUR"
        self.nama:str   = "Euro"
    
    # method untuk print object (overriding dengan parent)
    def toString(self):
        print(textKode, self.kode)
        print(textNama, self.nama)
        print(textNegara, self.negara)
        print(textAmount, self.simbol, locale.currency( self.amount, symbol=False, grouping=True ))