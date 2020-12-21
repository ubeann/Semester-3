# Creator:
# @Ubeannn  | 081911633071
import sys, os                  # import sys, os module untuk mengganti path directory
# mengganti path directory supaya bisa import file pada package 1
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//package1")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"//package2")
import C1,C2,C3,C4,C5       #import class C1-C5 untuk test running access class

#class C1
print("[class C1]".center(30,'-'))
c1 = C1.C1()
c1.nilai()
c1._m()

#class C2
print("[class C2]".center(30,'-'))
c2 = C2.C2()
c2.access()

#class C3
print("[class C3]".center(30,'-'))
c3 = C3.C3()
c3.access()

#class C4
print("[class C4]".center(30,'-'))
c4 = C4.C4()
c4.access()

#class C5
print("[class C5]".center(30,'-'))
c5 = C5.C5()
c5.access()

#credit
print("".center(30,'-'))
print("[ CREDIT ]".center(30,'-'))
print("[ @ubeannn ]".center(30,'-'))
print("[ 081911633071 ]".center(30,'-'))
print("[ Thank You ]".center(30,'-'))
print("".center(30,'-'))