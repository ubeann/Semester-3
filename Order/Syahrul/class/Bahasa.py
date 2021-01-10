# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 10 Januari 2021

from Kelas import Kelas   # import parent class

# child class Bahasa object (Single Inheritance)
class Bahasa(Kelas):
    # Constructor (Overriding & Overloading parameter from parent)
    def __init__(self, nama:str = "Bahasa", kuota:int = 0, guru:str = "Bapak"):
        super().__init__(nama, kuota)
        self.guru = guru

    # Overriding method from parent
    def action(self):
        super().action()
        print("Di kelas,", self.nama, " ini, kalian akan saya ajar selama semester ini")
        print("Perkenalkan saya,", self.guru)
        print("Diharap kalian dapat menikmati kelas ini")
    def describe(self):
        super().describe()
        print("Guru\t:", self.guru)