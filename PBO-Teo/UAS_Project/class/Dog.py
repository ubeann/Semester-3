# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

from Animal import Animal   #import parent class

# child class Dog object (Single Inheritance)
class Dog(Animal):
    # Constructor
    def __init__(self,name:str = "name", age:int = 0, detail:str ="It's a Dog"):
        super().__init__(name,age)  # call parent constructor
        self.detail = detail

    # Overiding method from parent
    def eat(self):
        print("[Dog eat()]".center(30,'-'))
        print("Dog",end='\t: ')
        super().eat()
        print("Dog",end='\t: ')
        print("Woff-woff")
    def string(self):
        print("[Property of Dog]".center(30,'-'))
        super().string()
        print("Detail\t: ", self.detail)
        print("".center(30,'-'))