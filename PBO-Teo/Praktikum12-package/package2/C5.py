# Creator:
# @Ubeannn  | 081911633071
import sys, os                  # import sys, os module untuk mengganti path directory
# mengganti path directory supaya bisa import C1
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-1]+"1")

import C1    # import C1 class pada "C1.py"

class C5:
    o = C1.C1()
    x = hasattr(o,'x')          # check acces variable C1
    y = hasattr(o,'_y')         # check acces variable C1
    z = hasattr(o,'z')          # check acces variable C1
    u = hasattr(o,'__u')        # check acces variable C1
    m = hasattr(o,'_m')         # check access m protected function
    def access(self):
        print("Can access o.x\t\t:",self.x)
        print("Can access o.y\t\t:",self.y)
        print("Can access o.z\t\t:",self.z)
        print("Can access o.u\t\t:",self.u)
        print("Can invoke o.m()\t:",self.m)