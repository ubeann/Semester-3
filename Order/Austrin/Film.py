""" Project UAS PBO Teori Semester 3
    Nama    : Austrin Bahirsyah
    NIM     : 081911633030            
    Hari/Tgl: Minggu, 17 Januari 2021   
    Topic   : Film Bioskop           """

# Class "film" akan menjadi parent class untuk film-film bioskop
class Film:

    # Constructor dengan Overloading parameter
    def __init__(self, publisher:str = "Austrin Bahirsyah", release:str = "Januari 2020"):
        self.publisher = publisher
        self.release   = release
    
    # Method yang akan di Overriding di class child
    def cetak(self):
        pass