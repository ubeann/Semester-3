# Nama      : Muhamad Erza Ranandha  
# NIM       : 081911633069           
# Hari, Tgl : Jum'at, 15 Januari 2021

# import parent class
from Buku import Buku

# Object 'CaraIPK4' child class dari parent class "Buku"
class CaraIPK4(Buku):
    # Constructor dengan parameter Overloading (Memiliki nilai default meskipun user tidak input)
    # dan Overriding dari parent class
    def __init__(self, author:str = "Erza Ranandha", publisher:str = "UNAIR", quantity:int = 1, price:int = 10):
        super().__init__(author, publisher)
        self.quantity  = quantity 
        self.price     = price
        self.judul     = "Cara IPK 4"
    
    # Overriding method
    def describe(self):
        print("Judul Buku:", self.judul)
        super().describe()
        print("Kuantitas :", self.quantity)
        print("Harga Buku: $", self.price)