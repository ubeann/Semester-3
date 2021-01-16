""" Project UAS PBO Teori Semester 3
    Nama    : Austrin Bahirsyah
    NIM     : 081911633030            
    Hari/Tgl: Minggu, 17 Januari 2021   
    Topic   : Film Bioskop           """

from Film import Film       # Import class yang dibutuhkan

# Class "Bioskop" akan menjadi list untuk film yang akan tayang
class Bioskop:

    # Contructor dengan Overloading parameter
    def __init__(self, brand:str = "Cinema XXI", owner:str = "Austrin Bahirsyah", lokasi:str = "Gresik"):
        self.brand     = brand
        self.owner     = owner
        self.lokasi    = lokasi
        self.film:list = []
    
    # Method untuk menambahkan film ke daftar
    def add(self, addfilm = None):
        if(issubclass(type(addfilm), type(Film()))):
            self.film.append(addfilm)
            print("Film berhasil ditambahkan:", addfilm.judul)
        else:
            print("Film yang diinput tidak ada, silahkan ulangi!")

    # Method untuk menghapus film pada daftar
    def remove(self, index:int = 0):
        if (len(self.film) != 0):
            if (index < len(self.film)):
                removed = self.film.pop(index)
                print("Film berhasil dihapus:", removed.judul)
            else:
                print("Index melebihi daftar, Film yg dipilih tidak ada")
        else:
            print("Daftar film masih kosong, remove() tidak akan berjalan")

    # Method untuk mencetak bioskop beserta film-filmnya
    def cetak(self):
        print("Brand :", self.brand)
        print("Owner :", self.owner)
        print("Lokasi:", self.lokasi)
        self.index = 1
        if (len(self.film) != 0):
            print("Daftar Film:")
            for i in self.film:
                print("-"*33)
                print(("[Film Ke-"+ str(self.index) +"]").center(33))
                i.cetak()
                self.index += 1
        else:
            print("Daftar Film: Kosong")