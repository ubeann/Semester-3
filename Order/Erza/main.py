# Nama      : Muhamad Erza Ranandha  
# NIM       : 081911633069           
# Hari, Tgl : Jum'at, 15 Januari 2021

# import class
from Buku               import Buku             # parent class
from CaraIPK4           import CaraIPK4         # child class
from LangitSeribu       import LangitSeribu     # child class
from SBMPTN             import SBMPTN           # child class
from SejarahIndonesia   import SejarahIndonesia # child class
from TiadaKasih         import TiadaKasih       # child class

# author
print("-"*35)
print("Nama      : Muhamad Erza Ranandha  ")
print("NIM       : 081911633069           ")
print("Hari, Tgl : Jum'at, 15 Januari 2021")
print("-"*35)

# main program
print("\n> CaraIPK4() untuk membuat objek buku", '"Cara IPK 4"')
buku1 = CaraIPK4("Epictetus", "PT. Gramedia", 3, 8)
print("> Objek buku telah dibuat")
print("> describe() untuk mengecek deskripsi pada buku")
print("-"*50)
buku1.describe()
print("-"*50)

# tanpa mengisi parameter "harga" untuk mengecek Overloading
print("\n> LangitSeribu() untuk membuat objek buku", '"Langit Seribu"')
buku2 = LangitSeribu("Peter Drucker", "Socios Inc.", 15)
print("> Objek buku telah dibuat")
print("> describe() untuk mengecek deskripsi pada buku")
print("-"*50)
buku2.describe()
print("-"*50)

# tanpa mengisi parameter "harga" dan "kuantitas" untuk mengecek Overloading
print("\n> SBMPTN() untuk membuat objek buku", '"SBMPTN"')
buku3 = SBMPTN("Maya Angelou", "Amazon.com")
print("> Objek buku telah dibuat")
print("> describe() untuk mengecek deskripsi pada buku")
print("-"*50)
buku3.describe()
print("-"*50)

# tanpa mengisi parameter "harga", "kuantitas", dan "pengarang" untuk mengecek Overloading
print("\n> SejarahIndonesia() untuk membuat objek buku", '"Sejarah Indonesia"')
buku4 = SejarahIndonesia("Norman Vincent Peale")
print("> Objek buku telah dibuat")
print("> describe() untuk mengecek deskripsi pada buku")
print("-"*50)
buku4.describe()
print("-"*50)

# tanpa mengisi parameter sama-sekali untuk mengecek Overloading
print("\n> TiadaKasih() untuk membuat objek buku", '"Tiada Kasih"')
buku5 = TiadaKasih()
print("> Objek buku telah dibuat")
print("> describe() untuk mengecek deskripsi pada buku")
print("-"*50)
buku5.describe()
print("-"*50)