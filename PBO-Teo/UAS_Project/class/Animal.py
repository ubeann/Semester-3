# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

#Class animal sebagai parent class untuk class lain
class Animal:
    # Constructor
    def __init__(self,name:str = "name", age:int = 0):
        self.name = name
        self.age = age
    def eat(self):
        print("Nyam-nyam-nyam")
    def string(self):
        print("Name\t\t: ", self.name)
        print("Age\t\t\t: ", self.age)