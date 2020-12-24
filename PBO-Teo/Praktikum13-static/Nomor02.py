# Creator:
# @Ubeannn  | 081911633071

class Animal:
    def __init__(self):
        self.cobaVarStatic = 25
    def eat(self):
        print("Menjalankan method eat()")
    class Mammal:
        def __init__(self):
            self.outer = Animal()
        def displayInfo(self):
            print("I am a mammal")
        @staticmethod
        def cekMethodStatic():
            print("Method static dicoba...")
        def mammalEat(self):
            print("In mammal class:", end=' ')
            self.outer.eat()
        def tampilVarStatic(self):
            print("In mammal class:", "cobaVarStatic =", self.outer.cobaVarStatic)
    class Reptile:
        def __init__(self):
            self.outer = Animal()
        def displayInfo(self):
            print("I am a reptile")
        def reptileEat(self):
            print("In reptile class:", end=' ')
            self.outer.eat()

# main code
print("[class Animal]".center(30,'-'))
a = Animal()        # membuat objek "Animal"
a.eat()             # menjalankan method "eat()"
print("[class Mammal]".center(30,'-'))
a.Mammal().displayInfo()        # class Mammal: menjalankan method "displayInfo()"
a.Mammal().cekMethodStatic()    # class Mammal: menjalankan method "cekMethodStatic()"
a.Mammal().mammalEat()          # class Mammal: menjalankan method "mammalEat()"
a.Mammal().tampilVarStatic()    # class Mammal: menjalankan method "tampilVarStatic()"
print("[class Reptile]".center(30,'-'))
a.Reptile().displayInfo()       # class Reptile: menjalankan method "displayInfo()"
a.Reptile().reptileEat()        # class Reptile: menjalankan method "reptileEat()"