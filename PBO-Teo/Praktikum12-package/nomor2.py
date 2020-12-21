# Creator:
# @Ubeannn  | 081911633071

# list library
import random as lib1           # 1
import math as lib2             # 2
import statistics as lib3       # 3
import datetime as lib4         # 4
import calendar as lib5         # 5

# class library 1 (random)
class Random:
    def randomfloat(self):
        # Random float:  0.0 <= x < 1.0
        print("random()\t=>","Random float value\t:",lib1.random())
    def randomint(self):
        # Random integer:  21 <= x <= 71
        print("randint()\t=>","Random integer value\t:",lib1.randint(21,71))
    def randomrange(self):
        # Random integer:  0 <= x <= 27
        print("randrange()\t=>","Random range value\t:",lib1.randrange(27))
    def randomchoice(self):
        # Single random element from a sequence
        print("choice()\t=>","Random choice value\t:",lib1.choice(['A','B','C','D','E']))
    def randomshuffle(self):
        # Shuffle a list
        sdata = ['A','B','C','D','E']
        lib1.shuffle(sdata)
        print("shuffle()\t=>","Random shuffle value\t:",sdata)

# class library 2 (math)
class Math:
    def mathsqrt(self):
        # Print the square root of x
        print("sqrt()\t\t=>","Math sqrt value (7.29)\t\t:",lib2.sqrt(7.29))
    def mathdegrees(self):
        # Convert angle x from radians to degrees
        print("degrees()\t=>","Math degrees value (3.14rad)\t:",lib2.degrees(3.14))
    def mathradians(self):
        # Convert angle x from degrees to radians
        print("radians()\t=>","Math radians value (180deg)\t:",lib2.radians(180))
    def mathsin(self):
        # Print the sine of x radians
        print("sin()\t\t=>","Math sin value (7.12)\t\t:",lib2.sin(7.12))
    def mathcos(self):
        # Print the cos of x radians
        print("cos()\t\t=>","Math cos value (1.72)\t\t:",lib2.cos(1.72))

# class library 3 (statistics)
class Statistics:
    def statmean(self):
        # Return the sample arithmetic mean of data
        print("mean()\t\t=>","Statistics mean value (1,2,3,4)\t\t:",lib3.mean([1,2,3,4]))
    def statmedian(self):
        # Return the median (middle value) of numeric data, using the common “mean of middle two” method
        print("median()\t=>","Statistics median value (1,2,3,4)\t:",lib3.median([1,2,3,4]))
    def statstdev(self):
        # Return the sample standard deviation (the square root of the sample variance)
        print()
c = Statistics()
c.statmean()
c.statmedian()

# b = Math()
# b.mathsqrt()
# b.mathdegrees()
# b.mathradians()
# b.mathsin()
# b.mathcos()

# a = Random()
# a.randomfloat()
# a.randomint()
# a.randomrange()
# a.randomchoice()
# a.randomshuffle()