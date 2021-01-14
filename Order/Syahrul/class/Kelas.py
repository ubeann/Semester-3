# Nama  : M. Syahrul A
# NIM   : 081911633037
# Tgl   : 10 Januari 2021

# Class Kelas sebagai parent class untuk class lain
class Kelas:
    # Constructor (Overloading parameter)
    def __init__(self, nama:str = "nama kelas", kuota:int = 0):
        self.nama = nama
        self.kuota = kuota
    def action(self):
        print("Selamat datang di kelas")
    def describe(self):
        print("Nama\t:", self.nama)
        print("Kuota\t:", self.kuota)