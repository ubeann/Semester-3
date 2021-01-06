# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

# import sys, os module for add path directory
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-5]+"//module")  # path for "module"  

from Cat import Cat         # import parent class
import ubean as module      # for call user-defined function

# descent class Persian object (Multi-level Inheritance: Persian => Cat => Animal)
class Persian(Cat):
    # Constructor
    def __init__(self,name:str = "name", age:int = 0, detail:str = "It's a Persian Cat", color:str = "white", size:str = "medium"):
        super().__init__(name,age,detail)  # call parent constructor
        self.color  = color
        self.size   = size

    # Overriding method from parent
    def eat(self, food:str = "Chips"):
        module.subtitle("Persian eat("+ food +")", width=18)
        print("Cat",end='\t: ')
        print("Meww-Meow")
        module.subtitle("Persian eat("+ food +")", False, width=18+len(food))
        print("*seems like", food)
    def string(self):
        super().string()
        print("Color\t\t: ", self.color)
        print("Size\t\t: ", self.size)