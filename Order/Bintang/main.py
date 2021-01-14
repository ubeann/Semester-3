""" Nama    : Bintang Muhammad Agastya
    NIM     : 081911633039            
    Hari/Tgl: Kamis, 14 Januari 2021   """

# import sys, os module for add path directory
import sys, os

# add path directory for import class in "class" directory and also module path
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//class")   # path for "class" 

# import class
from Item import Item           # Item class     (parent class)
from Backpack import Backpack   # Backpack class (child class inherit with "Item" parent class)
from Eraser import Eraser       # Eraser class   (child class inherit with "Item" parent class)
from Notebook import Notebook   # Notebook class (child class inherit with "Item" parent class)
from Pen import Pen             # Pen class      (child class inherit with "Item" parent class)
from Pencil import Pencil       # Pencil class   (child class inherit with "Item" parent class)
from Ruler import Ruler         # Ruler class    (child class inherit with "Item" parent class)

# credit
print("#"*34)
print("Nama    : Bintang Muhammad Agastya")
print("NIM     : 081911633039            ")
print("Hari/Tgl: Kamis, 14 Januari 2021  ")
print("#"*34)

# main program
print("\n-> Create Object Backpack")                      
item_list = Backpack(owner = "Bintang", capacity = 3)
item_list.detail()

print("\n-> Backpack.remove()")
item_list.remove()

print("\n-> Backpack.add() menambahkan Object Eraser")
item_list.add(Eraser(owner = "Bintang"))

print("\n-> Backpack.add() menambahkan Object Pen")
item_list.add(Pen(owner = "Agastya"))

print("\n-> Backpack.add() menambahkan Object Notebook")
item_list.add(Notebook(owner = "Bintang"))

print("\n-> Backpack.add() menambahkan Object Ruler")
item_list.add(Ruler(owner = "Agastya"))

print("\n-> Backpack.remove(4) pada index = 4")
item_list.remove(4)

print("\n-> Backpack.remove(1) pada index = 1")
item_list.remove(1)

print("\n-> Backpack.add() menambahkan Object Pencil")
item_list.add(Pencil(owner = "Bintang"))

print("\n-> Backpack.detail()")
item_list.detail()