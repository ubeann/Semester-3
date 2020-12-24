# Creator:
# @Ubeannn  | 081911633071

# Ubahlah inner class berikut menjadi outer class ?? (mengubah outer inner maupun sebaliknya)
class Engine:
    def __init__(self, carName, carType):
        self.carName = carName
        self.carType = carType
    def setEngine(self):
        if (self.carType == "4WD"):
            if (self.carName == "Crysler"):
                self.engineType = "Bigger"
            else:
                self.engineType = "Smaller"
        else:
            self.engineType = "Bigger"
    def getEngineType(self):
        return self.engineType
    class Car:
        def __init__(self, carName, carType):
            self.carName = carName
            self.carType = carType
        def getCarName(self):
            return self.carName

# main code
print("[Objek Car 1]".center(30,'-'))
Engine1 = Engine("Mazda","8WD")                     # membuat objek "Engine" (outer class)
Car1 = Engine1.Car(Engine1.carName,Engine1.carType) # membuat obejk "Car" (inner class)
Engine1.setEngine()                                 # menjalankan method "setEngine()"
print("Engine Type for 8WD =",Engine1.getEngineType())  # mencetak engineType Car1
print("[Objek Car 2]".center(30,'-'))
Engine2 = Engine("Crysler","4WD")                   # membuat objek "Engine" (outer class)
Car2 = Engine2.Car(Engine2.carName,Engine2.carType) # membuat obejk "Car" (inner class)
Engine2.setEngine()                                 # menjalankan method "setEngine()"
print("Engine Type for 4WD =",Engine2.getEngineType())  # mencetak engineType Car2