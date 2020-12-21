# Creator:
# @Ubeannn  | 081911633071
import C1       #import C1 class pada "C1.py"
class C2:
    o = C1.C1()                    # create object C1
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