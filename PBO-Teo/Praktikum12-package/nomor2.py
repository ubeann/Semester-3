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
        print("mean()\t\t=>","Statistics mean value (1,2,3,4)\t\t\t:",lib3.mean([1,2,3,4]))
    def statmedian(self):
        # Return the median (middle value) of numeric data, using the common “mean of middle two” method
        print("median()\t=>","Statistics median value (1,2,3,4)\t\t:",lib3.median([1,2,3,4]))
    def statstdev(self):
        # Return the sample standard deviation (the square root of the sample variance)
        print("stdev()\t\t=>","Statistics stdev value (1,2,3,4)\t\t\t:",lib3.stdev([1,2,3,4]))
    def statvarian(self):
        # Return the sample variance of data, an iterable of at least two real-valued numbers
        print("variance()\t=>","Statistics variance value (1,2,3,4)\t\t:",lib3.variance([1,2,3,4]))
    def statpvarian(self):
        # Return the population variance of data, a non-empty sequence or iterable of real-valued numbers
        print("pvariance()\t=>","Statistics p.variance value (1,2,3,4)\t:",lib3.pvariance([1,2,3,4]))

# class library 4 (datetime)
class DateTime:
    def datetoday(self):
        # Return the current local date
        print("today()\t\t\t=>","DateTime today value\t\t\t:",lib4.date.today())
    def datetime(self):
        # Return the current local datetime
        print("datetime()\t\t=>","DateTime datetime value\t\t:",lib4.datetime.now())
    def datectime(self):
        # Return a string representing the date:
        print("ctime()\t\t\t=>","DateTime ctime value\t\t\t:",lib4.datetime.today().ctime())
    def dateisocal(self):
        # Return a datetime corresponding to the ISO calendar date specified by year, week and day
        print("isocalendar()\t=>","DateTime isocalendar value\t:",lib4.datetime.today().isocalendar())
    def dateisoform(self):
        # Return a string representing the date in ISO 8601 format
        print("isoformat()\t\t=>","DateTime isoformat value\t\t:",lib4.date(2007,1,27).isoformat())

# class library 5 (calendar)
class Calendar:
    def calmonth(self):
        # Return a month of calendar
        print("month()\t=>","Calendar month value:\n",lib5.month(2021,7))
    def calwheader(self):
        # Return a header of week
        print("weekheader()\t=>","Calendar week header value\t:",lib5.weekheader(4))
    def calmonthrange(self):
        # Returns weekday of first day of the month and number of days in month, for the specified year and month
        print("monthrange()\t=>","Calendar month range value\t:",lib5.monthrange(2017,1))
    def calformont(self):
        # Return calendar of month with format
        print("formatmonth()\t=>","Calendar formatmonth value:\n",lib5.TextCalendar(lib5.FRIDAY).formatmonth(2017,1))
    def calpryear(self):
        # Print year of calendar
        print("pryear()\t=>","Calendar pryear value:")
        lib5.TextCalendar(lib5.SUNDAY).pryear(2017)

# main code
print("[Library Random]".center(65,'-'))
a = Random()
a.randomfloat()
a.randomint()
a.randomrange()
a.randomchoice()
a.randomshuffle()
print("")
print("[Library Math]".center(65,'-'))
b = Math()
b.mathsqrt()
b.mathdegrees()
b.mathradians()
b.mathsin()
b.mathcos()
print("")
print("[Library Statistics]".center(65,'-'))
c = Statistics()
c.statmean()
c.statmedian()
c.statstdev()
c.statvarian()
c.statpvarian()
print("")
print("[Library Date Time]".center(65,'-'))
d = DateTime()
d.datetoday()
d.datetime()
d.datectime()
d.dateisocal()
d.dateisoform()
print("")
print("[Library Calendar]".center(65,'-'))
e = Calendar()
e.calmonth()
e.calwheader()
e.calmonthrange()
e.calformont()
e.calpryear()