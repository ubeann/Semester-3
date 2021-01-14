""" Nama    : Bintang Muhammad Agastya
    NIM     : 081911633039
    Hari/Tgl: Kamis, 14 Januari 2021   """

from Item import Item       # Import Parent Class "Item"

# Child class yakni Object atau Class "Backpack" dengan Parent Class "Item"
class Backpack(Item):
    # Constructor (Overloading parameter)
    def __init__(self, owner:str = "User", capacity:int = 5):
        super().__init__(owner)
        self.capacity       = capacity
        self.inventory:list = []
    def add(self, additem = None):
        if (len(self.inventory) != self.capacity):
            if(issubclass(type(additem), type(Item()))):
                self.inventory.append(additem)
                print("Item berhasil ditambahkan:")
                additem.detail()
            else:
                print("Item tidak normal/tidak ada, silahkan ulangi!")
        else:
            print("Kapasitas pada Backpack telah full, silahkan hapus item terlebih dahulu")
    def remove(self, index:int = 0):
        if (len(self.inventory) != 0):
            if (index < self.capacity):
                removed = self.inventory.pop(index)
                print("Item berhasil dihapus:")
                removed.detail()
            else:
                print("Index melebihi kapasitas backpack, item yg dipilih tidak ada")
        else:
            print("Backpack masih kosong, remove() tidak akan berjalan")

    # Overriding method
    def detail(self):
        print("Item :","Backpack")
        print("Owner:", self.owner)
        print("Capacity:", self.capacity)
        if (len(self.inventory) != 0):
            print("Isi Backpack:", "\n"+"-"*10)
            for i in self.inventory:
                i.detail()
                print("-"*10)
        else:
            print("Isi Backpack: kosong")