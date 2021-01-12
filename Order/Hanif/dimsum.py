"""
PROJECT UAS PBO TEORI 

Nama        : Hanif Salvia Rachman
NIM         : 081911633077
Dibuat tgl  : 11 Januari 2021
"""
from menu import menu   # impor parent class

# child class from "menu" class
class dimsum(menu):
    #constructor
    def __init__(self, namaMenu:str, hargaMenu:int, bhnDasar:str, isi:int, topping:str = None):
        #Overloading
        if (topping != None):                       # Option while a user has written 'topping' value
            super().__init__(namaMenu, hargaMenu)
            self.topping = topping
        else:                                       # Option while a user hasn't written 'topping' value
            super().__init__(namaMenu, hargaMenu)
        self.bhnDasar = bhnDasar
        self.isi = isi
    
    def getBhnDasar(self):
        return self.bhnDasar
    
    def getIsi(self):
        return self.isi
    
    def getTopping(self):
        if hasattr(self, 'topping'):   # Overloading, check class has attribute 'topping'
            return self.topping
        else:
            return "None -> Overloading"

    def toString(self): # Overriding Method
        return str(super().toString() + " yang berupa olahan daging asli yang dikukus sehingga menghasilkan tekstur yang lembut dan rendah lemak.")

    def detailMenu(self):
        print("Nama Menu    : ", super().getNamaMenu())
        print("Bahan dasar  : ", self.getBhnDasar())
        print("Pilihan Topping  : ", self.getTopping())
        print("Isi per-pack : ", self.getIsi()," pcs")
        print("Harga        :  Rp.", super().getHargaMenu(),"per-pack")

    