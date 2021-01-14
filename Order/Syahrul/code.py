# Nama  : M. Syahrul A
# NIM   : 081911633037
# Tgl   : 10 Januari 2021

# import sys, os module for add path directory
import sys, os

# add path directory for import class in "class" directory and also module path
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//class")   # path for "class" 

# import class
from Kelas import Kelas         # Kelas class   (parent class)
from Bahasa import Bahasa       # Bahasa class  (child class inherit with "Kelas" parent class)
from Pbo import Pbo             # PBO class     (child class inherit with "Kelas" parent class)

# main code for running program
print("[Kelas Object]".center(40,"-"))      # Object 1 => Kelas
object1:Kelas = Kelas()                     # Create object type Kelas from "Kelas" class (parent class) --> using overloading paramater
print((" action("+") ").center(40,'+'))
object1.action()                            # Running action function in "Kelas" class
print((" describe("+") ").center(40,'+'))
object1.describe()                          # Running describe function in "Kelas" class
print('-'*40,"\n")
###################################################################################################################
print("[Bahasa Object]".center(40,"-"))                             # Object 2 => Bahasa
object2:Kelas = Bahasa("Bahasa Indonesia", 37, "Bapak Syahrul")      # Create object type Bahasa from "Bahasa" class (child class) --> polymorphism with "Kelas" object type
print(" action() ".center(40,'+'))
object2.action()                                                    # Running action function in "Bahasa" class --> Overriding method
print(" describe() ".center(40,'+'))
object2.describe()                                                  # Running describe function in "Bahasa" class --> Overriding method
print('-'*40,"\n")
###################################################################################################################
print("[PBO Object]".center(40,"-"))        # Object 3 => PBO
object3 = Pbo()                             # Create object type PBO from "PBO" class (child class) --> Overloading & Overriding in parameter
print(" action() ".center(40,'+'))
object3.action()                            # Running action function in "PBO" class --> Overriding method
print(" describe() ".center(40,'+'))
object3.describe()                          # Running describe function in "PBO" class --> Overriding method
print('-'*40)
###################################################################################################################
print("Create by:".center(40))
print("Nama\t:","M. Syahrul A")
print("NIM\t\t:",'081911633037')
print("Tgl\t\t:", '10 Januari 2021')
print('-'*40)