""" Nama    : Daffa Kenny Nabil Fayyaadh Priadi
    NIM     : 081911633040                     
    Hari/Tgl: Jum'at, 15 Januari 2021          """

# Class 'Pekerjaan' akan menjadi parent class untuk child class yang akan dibuat
class Pekerjaan:
    # Constructor Overloading
    def __init__(self, owner = None, gender = None):
        if (owner == None and gender == None):
            print("Owner dan Gender tidak diinputkan, dan akan diset secara default")
            print("Owner -> diberi nilai 'Bpk. Daffa Kenny' ")
            self.owner = "Bpk. Daffa Kenny"
            print("Gender-> diberi nilai 'L/P'")
            self.gender = "L/P"
        elif (gender == None):
            print("Gender tidak diinputkan, akan diset dengan nilai default 'L/P'")
            self.gender = "L/P"
            self.owner  = owner
        elif (owner == None):
            print("Owner tidak diinputkan, akan diset dengan nilai default 'Bpk. Daffa Kenny'")
            self.owner  = "Bpk. Daffa Kenny"
            self.gender = gender
        else:
            self.owner  = owner
            self.gender = gender

    # Overriding pada child class
    def cetak(self):
        print("Owner    :", self.owner)
        print("Gender   :", self.gender)