# Creator:
# @Ubeannn  | 081911633071
import sys                  # import sys module untuk mengganti path directory
sys.path.append("..")       # mengganti path directory supaya bisa import C1
# print(sys.path)
import C1    #import C1 class pada "C1.py"

# class C4(C1.C1):
#     x = hasattr(C1.C1,'x')          # check acces variable C1
#     y = hasattr(C1.C1,'_y')         # check acces variable C1
#     z = hasattr(C1.C1,'z')          # check acces variable C1
#     u = hasattr(C1.C1,'__u')        # check acces variable C1
#     m = hasattr(C1.C1,'_m')         # check access m protected function
#     def access(self):
#         print("Can access x\t\t:",self.x)
#         print("Can access y\t\t:",self.y)
#         print("Can access z\t\t:",self.z)
#         print("Can access u\t\t:",self.u)
#         print("Can invoke m()\t\t:",self.m)
# c = C4()
# c.access()