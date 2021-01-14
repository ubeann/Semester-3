""" Nama    : Bintang Muhammad Agastya
    NIM     : 081911633039
    Hari/Tgl: Kamis, 14 Januari 2021   """

from Item import Item       # Import Parent Class "Item"

# Child class yakni Object atau Class "Pen" dengan Parent Class "Item"
class Pen(Item):
    # Constructor (Overloading parameter)
    def __init__(self, owner:str = "User"):
        super().__init__(owner)
        self.nama = "Pen"

    # Overriding method
    def detail(self):
        print("Item :", self.nama)
        print("Owner:", self.owner)