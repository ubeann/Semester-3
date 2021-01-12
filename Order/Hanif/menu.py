"""
PROJECT UAS PBO TEORI 

Nama        : Hanif Salvia Rachman
NIM         : 081911633077
Dibuat tgl  : 11 Januari 2021
"""
from abc import ABC, abstractmethod

# parent class
class menu:
    #constructor
    def __init__(self, namaMenu:str, hargaMenu:int):
        self.namaMenu = namaMenu
        self.hargaMenu = hargaMenu

    def getNamaMenu(self):
        return self.namaMenu
    
    def getHargaMenu(self):
        return self.hargaMenu

    def toString(self):
        return self.namaMenu + " merupakan menu di Kedai77"
    
    # abstract method
    @abstractmethod
    def detailMenu(self):
        pass

   