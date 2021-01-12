"""
PROJECT UAS PBO TEORI 

Nama        : Hanif Salvia Rachman
NIM         : 081911633077
Dibuat tgl  : 11 Januari 2021
"""
from menu import menu   # impor parent class

# child class from "menu" class
class dessert(menu):
    #constructor
    def __init__(self, namaMenu:str, hargaMenu:int, varians:str, ukuran:str = None):
        #Overloading
        if (ukuran != None):                            # Option while a user has written 'ukuran' value
            super().__init__(namaMenu, hargaMenu)
            self.ukuran = ukuran
        else:                                           # Option while a user hasn't written 'ukuran' value
            super().__init__(namaMenu, hargaMenu)
        self.varians = varians
    
    def getUkuran(self):
        if hasattr(self, 'ukuran'):     # Overloading, check class has attribute 'ukuran'
            return self.ukuran
        else:
            return None
    
    def getVarians(self):
        return self.varians

    def toString(self): # Overriding Method
        return str(super().toString() + " yang tersedia dengan berbagai rasa. Dessert dengan rasa yang manis cocok dimakan bersama orang terdekat")

    def detailMenu(self):
        print("Nama Menu    : ", super().getNamaMenu())
        print("Varians rasa : ", self.getVarians())
        print("Harga        :  Rp.", super().getHargaMenu())
        if hasattr(self, 'ukuran'):     # Overloading, check class has attribute 'ukuran'
            print("Size         : ", self.getUkuran()," cm")
        else:
            print("Size         : ", self.getUkuran(), "--> Overloading")