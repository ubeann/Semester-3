# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

# import sys, os module for add path directory
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-5]+"//module")  # path for "module"  

from Animal import Animal   # import parent class
import ubean as module      # for call user-defined function

# child class Dog object (Single Inheritance)
class Dog(Animal):
    # Constructor
    def __init__(self,name:str = "name", age:int = 0, detail:str = "It's a Dog"):
        super().__init__(name,age)  # call parent constructor
        self.detail = detail

    # Overriding & Overloading method from parent
    def eat(self, food:str = ''):
        if len(food) == 0:          # here Overriding method
            print("Dog",end='\t: ')
            super().eat()
            module.subtitle("Dog "+"eat()", False, width=14)
            print("Dog",end='\t: ')
            print("Woff-woff")
        #########################################################
        else:                       # here Overloading method
            favorite = ["chips","choco","meat","sereal"]
            if food.casefold() in favorite:
                module.subtitle("Dog"+" eat("+ food +")", width=14)
                print("Dog",end='\t: ')
                print("Wofffff")
                module.subtitle("Dog"+" eat("+ food +")", False, width=14+len(food))
                print("*seems like", food)
            else:
                module.subtitle("Dog eat("+ food +")", width=14)
                print("Dog",end='\t: ')
                print("Hoekkk")
                module.subtitle("Dog eat("+ food +")", False, width=14+len(food))
                print("*seems hate", food)

    # Overriding method from parent
    def string(self):
        super().string()
        print("Detail\t: ", self.detail)