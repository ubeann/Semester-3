# Creator:
# @Ubeannn  | 081911633071

class TestOuter1:
    def __init__(self):
        self.data = 30
    class Inner:
        def __init__(self):
            self.outer = TestOuter1()    
        def msg(self):
            print("[Object TestOuter1 created]".center(35,'-'))
            print("Data is", self.outer.data)
class TestOuter1Inner:
    def __init__(self):
        self.TestOuter1 = TestOuter1()
    def msg(self):
        print("[Object TestOuter1$Inner created]".center(35,'-'))
        print("Data is",self.TestOuter1.data)

# main code
a = TestOuter1().Inner()    # membuat objek "TestOuter1"
a.msg()                     # menjalankan method msg()

b = TestOuter1Inner()       # membuat objek "TestOuter1$Inner"
b.msg()                     # menjalankan method msg()