# Creator:
# @Ubeannn  | 081911633071
import paket1    #import paket1 untuk parent class

class C4(paket1.C1):
    x = hasattr(paket1.C1,'x')         # check acces variable C1
    y = hasattr(paket1.C1,'_y')        # check acces variable C1
    z = hasattr(paket1.C1,'z')         # check acces variable C1
    u = hasattr(paket1.C1,'__u')       # check acces variable C1
    m = hasattr(paket1.C1,'_m')       # check access m protected function
    def access(self):
        print("Can access x\t\t:",self.x)
        print("Can access y\t\t:",self.y)
        print("Can access z\t\t:",self.z)
        print("Can access u\t\t:",self.u)
        print("Can invoke m()\t\t:",self.m)

class C5:
    o = paket1.C1()
    x = hasattr(o,'x')          # check acces variable C1
    y = hasattr(o,'_y')         # check acces variable C1
    z = hasattr(o,'z')          # check acces variable C1
    u = hasattr(o,'__u')        # check acces variable C1
    m = hasattr(o,'_m')        # check access m protected function
    def access(self):
        print("Can access o.x\t\t:",self.x)
        print("Can access o.y\t\t:",self.y)
        print("Can access o.z\t\t:",self.z)
        print("Can access o.u\t\t:",self.u)
        print("Can invoke o.m()\t:",self.m)