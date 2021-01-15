""" Nama    : Daffa Kenny Nabil Fayyaadh Priadi
    NIM     : 081911633040                     
    Hari/Tgl: Jum'at, 15 Januari 2021          """

# Import class
from Parent import Pekerjaan                            # Parent Class
from Child import Dosen, Gamer, Presiden, WebDeveloper  # Child Class

# Author
print("+---------------------------------------------+")
print("| Nama    : Daffa Kenny Nabil Fayyaadh Priadi |")
print("| NIM     : 081911633040                      |")
print("| Hari/Tgl: Jum'at, 15 Januari 2021           |")
print("+---------------------------------------------+")

# Main Code
print("\n-> Dosen() Membuat Pekerjaan Dosen")
dosen = Dosen("UNAIR", "Laki-Laki", 8000000, "Mengajar PBO")
print("-> Object Dosen telah dibuat.")
print("-> cetak() pada object Dosen untuk mengecek variable dosen")
dosen.cetak()
print("-----------------------------------------------")

# cek overloading tanpa input variable JobDesk
print("\n-> Gamer() Membuat Pekerjaan Gamer")
gamer = Gamer("OG", "Laki-Laki", 6500000)        
print("-> Object Gamer telah dibuat.")
print("-> cetak() pada object Gamer untuk mengecek variable Gamer")
gamer.cetak()
print("-----------------------------------------------")

# cek overloading tanpa input variable JobDesk dan Gaji
print("\n-> WebDeveloper() Membuat Pekerjaan Web Developer")
web = WebDeveloper("Riliv", "Wanita")        
print("-> Object WebDeveloper telah dibuat.")
print("-> cetak() pada object WebDeveloper untuk mengecek variable WebDeveloper")
web.cetak()
print("-----------------------------------------------")

# cek overloading tanpa input variable sama-sekali
print("\n-> Presiden() Membuat Pekerjaan Presiden")
presiden = Presiden()        
print("-> Object Presiden telah dibuat.")
print("-> cetak() pada object Presiden untuk mengecek variable Presiden")
presiden.cetak()
print("-----------------------------------------------")