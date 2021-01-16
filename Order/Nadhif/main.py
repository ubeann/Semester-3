# Project UAS PBO Teori
# Nama      : Nadhif Hakiim Risantosa
# NIM       : 081911633070
# Hari, Tgl : Jum'at, 17 Januari 2021

# import class
from Parent import MataUang     # parent class
from Child import Rupiah        # child class
from Child import DollarUS      # child class
from Child import Yuan          # child class
from Child import Euro          # child class
from Konversi import Konversi   # class -> untuk melakukan konversi

# print data diri
print("Nama     : Nadhif Hakiim Risantosa")
print("NIM      : 081911633070           ")
print("Hari, Tgl: Jum'at, 17 Januari 2021","\n") #34

# main
# menjalankan konstruktor tanpa parameter (uji overloading)
print("# obj = Konversi()")
obj = Konversi()
print("# obj.toString()")
obj.toString()
print()

# membuat sejumlah uang
print("# uang1 = Rupiah('Indonesia', 1500000)")
uang1 = Rupiah("Indonesia", 1500000)
print("# uang1.toString()")
uang1.toString()
print()

print("# uang2 = DollarUS(amount = 45000)")
uang2 = DollarUS(amount = 4500)
print("# uang2.toString()")
uang2.toString()
print()

# melakukan konversi
print("# obj.hitung(uang1, Euro())")
obj.hitung(uang1, Euro())
print()

print("# obj.hitung(uang2, Rupiah())")
obj.hitung(uang2, Rupiah())
print()

# uji overloading
print("# obj.hitung(uang1)")
obj.hitung(uang1)
print()
print("# obj.hitung()")
obj.hitung()
print()