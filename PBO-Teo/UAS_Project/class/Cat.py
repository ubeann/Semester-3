# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

# import sys, os module for add path directory
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-5]+"//module")  # path for "module"  

from Animal import Animal   # import parent class
import ubean as module      # for call user-defined function

# child class Cat object (Single Inheritance)
class Cat(Animal):
    # Constructor
    def __init__(self,name:str = "name", age:int = 0, detail:str = "It's a cat"):
        super().__init__(name,age)  # call parent constructor
        self.detail = detail

    # Overriding method from parent
    def eat(self):
        print("Cat",end='\t: ')
        super().eat()
        module.subtitle("Cat eat()", False, width=14)
        print("Cat",end='\t: ')
        print("Meowwww")
    def string(self):
        super().string()
        print("Detail\t: ", self.detail)