# Creator:
# @Ubeannn  | 081911633071
class C1:
    x = None                        # public int x
    _y = None                       # protected int y
    z = None                        # int z
    __u = None                      # private int u
    def _m(self):                  # protected void m()
        print("method protected void m()")
    def nilai(self):                # method cek nilai
        print("Nilai x\t:",self.x)
        print("Nilai y\t:",self._y)
        print("Nilai z\t:",self.z)
        print("Nilai u\t:",self.__u)

class C2:
    o = C1()                    # create object C1
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

class C3(C1):
    x = hasattr(C1,'x')         # check acces variable C1
    y = hasattr(C1,'_y')        # check acces variable C1
    z = hasattr(C1,'z')         # check acces variable C1
    u = hasattr(C1,'__u')       # check acces variable C1
    m = hasattr(C1,'_m')       # check access m protected function
    
    # x = super().__getattribute__('x')
    # y = super().__getattribute__('_y')
    # z = super().__getattribute__('z')
    # u = super().__getattribute__('__u')
    # m = super().__getattribute__('__m')
    def access(self):
        print("Can access x\t\t:",self.x)
        print("Can access y\t\t:",self.y)
        print("Can access z\t\t:",self.z)
        print("Can access u\t\t:",self.u)
        print("Can invoke m()\t\t:",self.m)