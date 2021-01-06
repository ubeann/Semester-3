# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021

# import sys, os module for add path directory
import sys, os        

# add path directory for import class in "class" directory and also module path
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//class")   # path for "class"  
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//module")  # path for "module"  

# import class
from Animal import Animal     # Animal class  (parent class)
from Cat import Cat           # Cat class     (child class inherit with "Animal" parent class)
from Dog import Dog           # Dog class     (child class inherit with "Animal" parent class)
from Persian import Persian   # Persian class (descent class, Multi-level Inheritance: Persian => Cat => Animal)

# import module user-defined
import ubean as module                  # for call user-defined function

# main code for running program
module.title("Object Animal")           # Object 1 => Animal
object1:Animal = Animal("Budy",2)       # Create object type Animal from "Animal" class (parent class)
module.subtitle("Animal eat()")
object1.eat()                           # Running eat function in "Animal" class
module.title("Properties Animal")
object1.string()                        # Running string function in "Animal" class
module.line(char='-')
print("")
###################################################################################################################
module.title("Object Cat")                  # Object 2 => Cat
object2:Animal = Cat("Ubean",81911633017)   # Create object type Cat from "Cat" class (child class, parent: Animal)
module.subtitle("Cat eat()", width=12)
object2.eat()                               # Running eat function in "Cat" class (Overriding function)
module.title("Properties Cat")
object2.string()                            # Running string function in "Cat" class (Overriding function)
module.line(char='-')
print("")
###################################################################################################################
module.title("Object Dog")              # Object 3 => Dog
object3:Dog = Dog("Orote",14)           # Create object type Dog from "Dog" class (child class, parent: Animal)
module.subtitle("Dog eat()", width=12)
object3.eat()                           # Running eat function in "Dog" class (Overriding function)
object3.eat('Patty')                    # Running eat function in "Dog" class (Overloading function)
module.title("Properties Dog")
object3.string()                        # Running string function in "Dog" class (Overriding function)
module.line(char='-')
print("")
###################################################################################################################
module.title("Object Persian")                                          # Object 4 => Persian
object4:Persian = Persian("Fannathic",17,color="White",size="Large")    # Create object type Persian from "Persian" class (child class, parent: Animal)
object4.eat('Chips')                                                    # Running eat function in "Persian" class (Overloading function)
module.title("Properties Persian")
object4.string()                                                        # Running string function in "Persian" class (Overriding function)
module.line(char='-')
print("")

# Credit
module.credit()