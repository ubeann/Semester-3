"""
PROJECT UAS PBO TEORI 

Nama        : Hanif Salvia Rachman
NIM         : 081911633077
Dibuat tgl  : 11 Januari 2021
"""
from menu import menu   # impor parent class

# child class from "menu" class
class beverage(menu):
    #constructor
    def __init__(self, namaMenu:str, hargaMenu:int, varians:str, size:str = None):
        #Overloading
        if (size != None):                          # Option while a user has written 'size' value
            super().__init__(namaMenu, hargaMenu)
            self.size = size
        else:                                       # Option while a user hasn't written 'topping' value
            super().__init__(namaMenu, hargaMenu)
        self.varians = varians
    
    def getSize(self):
        if hasattr(self, 'size'):   # Overloading, check class has attribute 'size'
            return self.size
        else:
            return None
    
    def getVarians(self):
        return self.varians

    def toString(self): # Overriding Method
        return str(super().toString() + " yang tersedia dengan berbagai rasa. Beverage di toko kami sangat cocok untuk dinikmati sambil bersantai")

    def detailMenu(self):
        print("Nama Menu    : ", super().getNamaMenu())
        print("Varians rasa : ", self.getVarians())
        print("Harga        :  Rp.", super().getHargaMenu())
        if hasattr(self, 'size'):   # Overloading, check class has attribute 'size'
            print("Size         : ", self.getSize()," ml")
        else:
            print("Size         : ", self.getSize(), "--> Overloading")