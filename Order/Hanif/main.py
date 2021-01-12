"""
PROJECT UAS PBO TEORI 

Nama        : Hanif Salvia Rachman
NIM         : 081911633077
Dibuat tgl  : 11 Januari 2021
"""
from menu import menu           # parent class
from dessert import dessert     # child class
from beverage import beverage   # child class
from dimsum import dimsum       # child class

print("\nDAFTAR MENU KEDAI77 \nOleh : Hanif Salvia Rachman - 081911633077 \n--------------------------------------------------------------------")
print(">> DESSERT")
print()
dessert1 = dessert("Layer Cake", 35000,"Coklat, Vanilla, Matcha", "diameter 15") #--> pake ukuran
dessert1.detailMenu()
print("Ket   "+"       : ", dessert1.toString(),"\n")
dessert2 = dessert("Dessert Box", 75000,"Red Velvet, Cheese Cream, Lotus", None) #--> gapake ukuran
dessert2.detailMenu()
print("Ket  "+"        : ", dessert2.toString(),"\n")

print("--------------------------------------------------------------------\n")
print(">> BEVERAGE")

beverage1 = beverage("Coffe",  12500,"Latte, Expresso", "500") #--> pake size
beverage1.detailMenu()
print("Ket    "+"      : ", beverage1.toString(),"\n")
beverage2 = beverage("Juice",  10500,"Jus jambu, Jus mangga", None) #--> gapake size
beverage2.detailMenu()
print("Ket      "+"    : ", beverage2.toString(),"\n")

print("--------------------------------------------------------------------\n")
print(">> DIMSUM")

dimsum1 = dimsum("Hakau",10000,"seafood (udang)", 3,"Mayo, saos tomat, saos sambal") #--> pake topping
dimsum1.detailMenu()
print("Ket          : ", dimsum1.toString(),"\n")
dimsum2 = dimsum("Gyoza", 3300,"Daging ayam dan sayuran",6,None) #--> gapake topping
dimsum2.detailMenu()
print("Ket          : ", dimsum2.toString(),"\n")