# Project UAS PBO Teori
# Nama      : Nadhif Hakiim Risantosa
# NIM       : 081911633070
# Hari, Tgl : Jum'at, 17 Januari 2021

from Parent import MataUang                     # import parent class
from Child import Rupiah, DollarUS, Yuan, Euro  # import child class

# class konversi akan mengonversi object-object mata uang ke mata uang yang lain
class Konversi:
    # konstruktor dengan parameter overloading (memiliki nilai default)
    def __init__(self, merk:str = "Nadhif Exchange", pemilik:str = "Nadhif Hakiim Risantosa"):
        self.merk      = merk
        self.pemilik   = pemilik
        self.pair:dict = { 
            # kurs mata uang
            "IDR/EUR" : 17095,
            "IDR/USD" : 14152,
            "IDR/CNY" : 2183,
            "USD/EUR" : 1.21,
            "USD/CNY" : 0.15,
            "USD/IDR" : 0.000071,
            "EUR/USD" : 0.83,
            "EUR/CNY" : 0.13,
            "EUR/IDR" : 0.000000585,
            "CNY/EUR" : 7.83,
            "CNY/USD" : 6.48,
            "CNY/IDR" : 0.00046
        }

    # method untuk menghitung
    def hitung(self, asal = None, tujuan = None):
        if (asal != None and tujuan != None):
            if (not issubclass(type(tujuan), type(MataUang()))):
                print("Mata uang tujuan tidak didukung")
            elif (not issubclass(type(asal), type(MataUang()))):
                print("Mata uang asal tidak didukung")
            else:
                key = asal.kode + "/" + tujuan.kode
                print("Mata Uang Asal".center(34))
                asal.toString()
                print("".center(34,'-'))
                print("Mata Uang Hasil".center(34))
                if (tujuan.kode == "IDR"):
                    Rupiah(amount = round(asal.amount / self.pair[key])).toString()
                elif (tujuan.kode == "USD"):
                    DollarUS(amount = round(asal.amount / self.pair[key],2)).toString()
                elif (tujuan.kode == "CNY"):
                    Yuan(amount = round(asal.amount / self.pair[key],2)).toString()
                else:
                    Euro(amount = round(asal.amount / self.pair[key],2)).toString()
        elif (asal != None):
            print("Mata uang tujuan tidak diinputkan, method error")
        else:
            print("Mata uang asal & tujuan tidak diinputkan, method error")   

    # method untuk print object
    def toString(self):
        print("Nama Usaha:", self.merk)
        print("Pemilik   :", self.pemilik)