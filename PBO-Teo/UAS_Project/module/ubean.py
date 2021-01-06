# Nama  : Muhammad Rizal Bagus Prakasa
# NIM   : 081911633071
# Tgl   : 6 Januari 2021 

# variable controller
myIdentity:dict = {
    "name"  :   "Muhammad Rizal Bagus Prakasa",
    "nim"   :   "081911633071",
    "tgl"   :   "Rabu, 6 Januari 2021",
    "sign"  :   ["Nama  :", "NIM   :", "Tgl   :"]
}
lineLength:int  = 45
lineChar:str    = '#'
titleSign:str   = '[]'      # string length = 2, ex: "[]" or "{}" and etc 
titleChar:str   = '-'
subLength:int   = 16
creditSign:str  = '#'

# Title user-defined function
def title(title:str = ''):
    print((titleSign[:1] + title + titleSign[-1:]).center(lineLength, titleChar))

# Title user-defined function
def subtitle(title:str = '', show:bool = True, width:int = subLength):
    if (show):
        print(title, space(width-4, title), end = "---> ")
    else:
        print(space(width-4), end = "---> ")

# Line user-defined function
def line(width:int = lineLength, char:str = lineChar):
    print(''.center(width, char))

# Space user-defined function
def space(width:int = 0, string:str = ''):
    return ''.center(width-len(string))

# Credit user-defined function
def credit():
    line()
    print(creditSign, myIdentity["sign"][0], myIdentity["name"], space(lineLength-5, myIdentity["sign"][0] + myIdentity["name"]), end = '#\n')
    print(creditSign, myIdentity["sign"][1], myIdentity["nim"], space(lineLength-5, myIdentity["sign"][1] + myIdentity["nim"]), end = '#\n')
    print(creditSign, myIdentity["sign"][2], myIdentity["tgl"], space(lineLength-5, myIdentity["sign"][2] + myIdentity["tgl"]), end = '#\n')
    line()