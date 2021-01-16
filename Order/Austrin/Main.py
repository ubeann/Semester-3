""" Project UAS PBO Teori Semester 3
    Nama    : Austrin Bahirsyah
    NIM     : 081911633030            
    Hari/Tgl: Minggu, 17 Januari 2021   
    Topic   : Film Bioskop           """

# import class
from Bioskop      import Bioskop        # class yang akan menjadi list film
from Film         import Film           # parent class, untuk film-film di bawah
from Gambit       import Gambit         # merupakan child class dari "film"
from Interstellar import Interstellar   # merupakan child class dari "film"
from Joker        import Joker          # merupakan child class dari "film"
from Lupin        import Lupin          # merupakan child class dari "film"
from Mandalorian  import Mandalorian    # merupakan child class dari "film"
from Wonder       import Wonder         # merupakan child class dari "film"

# cetak detail program
print("Project UAS PBO Teori Semester 3")
print("-"*33, end = "")
print("""
Nama    : Austrin Bahirsyah
NIM     : 081911633030            
Hari/Tgl: Minggu, 17 Januari 2021   
Topic   : Film Bioskop           
""")

# main program
# tanpa parameter untuk menguji overloading konstruktor
print("-> Bioskop() : Membuat object Bioskop")
bioskop = Bioskop()
print("Object berhasil dibuat\n")

print("-> cetak() : mencetak object Bioskop")
bioskop.cetak()
print()

# dengan parameter lengkap atau sempurna
print("-> add() Bioskop dengan Object Film Gambit()")
bioskop.add(Gambit("Netflix", "Oktober 2020", 4.3, "Drama, Sport", "Senin, Selasa, dan Rabu"))
print()

# tanpa parameter jadwal (menguji overloading)
print("-> add() Bioskop dengan Object Film Interstellar()")
bioskop.add(Interstellar("Christopher Nolan", "November 2014", 4.3, "Adventure, Drama, Sci-Fi"))
print()

# tanpa parameter jadwal, dan genre (menguji overloading)
print("-> add() Bioskop dengan Object Film Joker()")
bioskop.add(Joker("Todd Phillips", "Oktober 2019", 4.25))
print()

# tanpa parameter jadwal, genre, dan rating (menguji overloading)
print("-> add() Bioskop dengan Object Film Lupin()")
bioskop.add(Lupin("Netflix", "2021"))
print()

# tanpa parameter jadwal, genre, rating, dan release (menguji overloading)
print("-> add() Bioskop dengan Object Film Mandalorian()")
bioskop.add(Mandalorian("Netflix"))
print()

# tanpa parameter sama sekali (menguji overloading)
print("-> add() Bioskop dengan Object Film Wonder()")
bioskop.add(Wonder())
print()

print("-> cetak() : mencetak object Bioskop")
bioskop.cetak()