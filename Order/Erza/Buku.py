# Nama      : Muhamad Erza Ranandha  
# NIM       : 081911633069           
# Hari, Tgl : Jum'at, 15 Januari 2021

# Object 'Buku' akan menjadi parent class
class Buku:
    # Constructor dengan parameter Overloading (Memiliki nilai default meskipun user tidak input) 
    # dan akan di Overriding di child class
    def __init__(self, author:str = "Erza Ranandha", publisher:str = "UNAIR"):
        self.author = author
        self.publisher  = publisher
    
    # Overriding method pada child class
    def describe(self):
        print("Author    :", self.author)
        print("Publisher :", self.publisher)