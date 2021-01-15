""" Nama    : Daffa Kenny Nabil Fayyaadh Priadi
    NIM     : 081911633040                     
    Hari/Tgl: Jum'at, 15 Januari 2021          """

# import parent class
from Parent import Pekerjaan

# Class 'Dosen' akan menjadi child class dengan parent class "Pekerjaan"
class Dosen(Pekerjaan):
    # Constructor Overloading dan Overriding dengan super() atau parent class
    def __init__(self, owner = None, gender = None, gaji = None, jobdesk = None):
        if (gaji != None and jobdesk != None):
            self.jobdesk = jobdesk
            self.gaji    = gaji
            super().__init__(owner, gender)
        elif (gaji != None):
            print("Jobdesk tidak diinputkan, akan diset dengan nilai default 'Minum Kopi'")
            self.jobdesk = "Minum Kopi"
            self.gaji    = gaji
            super().__init__(owner, gender)
        else:
            print("Jobdesk dan Gaji tidak diinputkan, akan diset dengan nilai default")
            print("Gaji    -> diberi nilai '1500000' ")
            self.gaji    = 1500000
            print("Jobdesk -> diberi nilai 'Minum Kopi' ")
            self.jobdesk = "Minum Kopi"
            super().__init__(owner, gender)

    # Overriding method
    def cetak(self):
        print("Pekerjaan:", "Dosen")
        super().cetak()
        print("Gaji     : Rp.", self.gaji)
        print("Job Desk :", self.jobdesk)

# Class 'WebDeveloper' akan menjadi child class dengan parent class "Pekerjaan"
class WebDeveloper(Pekerjaan):
    # Constructor Overloading dan Overriding dengan super() atau parent class
    def __init__(self, owner = None, gender = None, gaji = None, jobdesk = None):
        if (gaji != None and jobdesk != None):
            self.jobdesk = jobdesk
            self.gaji    = gaji
            super().__init__(owner, gender)
        elif (gaji != None):
            print("Jobdesk tidak diinputkan, akan diset dengan nilai default 'Nyantai di depan laptop'")
            self.jobdesk = "Nyantai di depan laptop"
            self.gaji    = gaji
            super().__init__(owner, gender)
        else:
            print("Jobdesk dan Gaji tidak diinputkan, akan diset dengan nilai default")
            print("Gaji    -> diberi nilai '7500000' ")
            self.gaji    = 7500000
            print("Jobdesk -> diberi nilai 'Nyantai di depan laptop' ")
            self.jobdesk = "Nyantai di depan laptop"
            super().__init__(owner, gender)

    # Overriding method
    def cetak(self):
        print("Pekerjaan:", "Web Developer")
        super().cetak()
        print("Gaji     : Rp.", self.gaji)
        print("Job Desk :", self.jobdesk)

# Class 'Gamer' akan menjadi child class dengan parent class "Pekerjaan"
class Gamer(Pekerjaan):
    # Constructor Overloading dan Overriding dengan super() atau parent class
    def __init__(self, owner = None, gender = None, gaji = None, jobdesk = None):
        if (gaji != None and jobdesk != None):
            self.jobdesk = jobdesk
            self.gaji    = gaji
            super().__init__(owner, gender)
        elif (gaji != None):
            print("Jobdesk tidak diinputkan, akan diset dengan nilai default 'Main Game'")
            self.jobdesk = "Main Game"
            self.gaji    = gaji
            super().__init__(owner, gender)
        else:
            print("Jobdesk dan Gaji tidak diinputkan, akan diset dengan nilai default")
            print("Gaji    -> diberi nilai '3750000' ")
            self.gaji    = 3750000
            print("Jobdesk -> diberi nilai 'Main Game' ")
            self.jobdesk = "Main Game"
            super().__init__(owner, gender)

    # Overriding method
    def cetak(self):
        print("Pekerjaan:", "Pro Player")
        super().cetak()
        print("Gaji     : Rp.", self.gaji)
        print("Job Desk :", self.jobdesk)

# Class 'Presiden' akan menjadi child class dengan parent class "Pekerjaan"
class Presiden(Pekerjaan):
    # Constructor Overloading dan Overriding dengan super() atau parent class
    def __init__(self, owner = None, gender = None, gaji = None, jobdesk = None):
        if (gaji != None and jobdesk != None):
            self.jobdesk = jobdesk
            self.gaji    = gaji
            super().__init__(owner, gender)
        elif (gaji != None):
            print("Jobdesk tidak diinputkan, akan diset dengan nilai default 'Ngatur Negara'")
            self.jobdesk = "Ngatur Negara"
            self.gaji    = gaji
            super().__init__(owner, gender)
        else:
            print("Jobdesk dan Gaji tidak diinputkan, akan diset dengan nilai default")
            print("Gaji    -> diberi nilai '1000000000' ")
            self.gaji    = 1000000000
            print("Jobdesk -> diberi nilai 'Ngatur Negara' ")
            self.jobdesk = "Ngatur Negara"
            super().__init__(owner, gender)

    # Overriding method
    def cetak(self):
        print("Pekerjaan:", "Presiden")
        super().cetak()
        print("Gaji     : Rp.", self.gaji)
        print("Job Desk :", self.jobdesk)