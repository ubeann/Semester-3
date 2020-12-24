# Creator:
# @Ubeannn  | 081911633071

# Ubahlah inner class berikut menjadi outer class ?? (mengubah outer inner maupun sebaliknya)
class Book:
    def __init__(self, bookName):
        self.bookName = bookName
    def getBookName(self):
        return self.bookName

class BookNode:
    def __init__(self,book:Book):
        self.book = book
        self.next:BookNode
    class BookList:
        def __init__(self):
            self._list = []
            self.tmpNode:BookNode
        def add(self, book:Book):
            self.node = BookNode(book)
            self._list.append(self.node)
        def toString(self):
            self.str = ""
            for x in self._list:
                self.str += (x.book.getBookName() + "\n")
            return self.str
# main code
BookShelf = BookNode(Book("Fali")).BookList()       # membuat objek "BookList" untuk list Book
# menambahkan books yg diminta
BookShelf.add(Book("Harry Potter"))
BookShelf.add(Book("Around the World in 80 Days"))
BookShelf.add(Book("Count of Monte Cristo"))
BookShelf.add(Book("Jataka Tales"))
BookShelf.add(Book("Aesop's Fables"))
# mencetak "BookShelf" dengan method "toString()" yg telah dibuat
print(BookShelf.toString())