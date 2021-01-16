""" Project UAS PBO Teori Semester 3
    Nama    : Austrin Bahirsyah
    NIM     : 081911633030            
    Hari/Tgl: Minggu, 17 Januari 2021   
    Topic   : Film Bioskop           """

from Film import Film       # Import class parent

# Class "Lupin" merupakan sub-class dari "Film"
class Lupin(Film):

    # Constructor dengan Overloading parameter dan Overriding dengan parent
    def __init__(self, publisher:str = "Austrin Bahirsyah", release:str = "Januari 2020", rating:float = 3.0, genre:str = "Comedy, Action",jadwal:str = "Rabu, Kamis, Jum'at"):
        super().__init__(publisher, release)
        self.judul:str = "Lupin"
        self.rating    = rating
        self.genre     = genre
        self.jadwal    = jadwal
    
    # Method yang akan di Overriding di class child
    def cetak(self):
        print("Judul    :", self.judul)
        print("Penerbit :", self.publisher)
        print("Rilis    :", self.release)
        print("Rating   :", str(self.rating) + "/5")
        print("Genre    :", self.genre)
        print("Jadwal   :", self.jadwal)