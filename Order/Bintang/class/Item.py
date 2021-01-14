""" Nama    : Bintang Muhammad Agastya
    NIM     : 081911633039
    Hari/Tgl: Kamis, 14 Januari 2021   """

# Parent class yakni Object atau Class "Item"
class Item:

    # Constructor (Overloading parameter)
    def __init__(self, owner:str = "User"):
        self.owner = owner
    
    # akan Overriding di child class
    def detail(self):
        pass