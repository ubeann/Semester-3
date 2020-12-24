// @ubeannn
// 081911633071

package percobaan10;
import java.io.*;   // mengimport package "IO" karena diperlukan untuk handling error yg terjadi

// menerapkan IOException ketika membuat objek dari class "RandomAccessFile" (java.io) yang menghasilkan file txt.

class RandomAccessRevisi {
    public static void main(String[] args) {
        String bookList[]={"Satu","Dua","Tiga"};
        int yearList[]={1920,1230,1940};
        try {
            // error "IO" terjadi dikarenakan tidak ada file dengan nama "books.txt"
            // handling yg dilakukan yakni membuat file baru dengan nama "books.txt"
            RandomAccessFile books = new RandomAccessFile ("books.txt","rw"); 

            // melanjutkan code flow dibawah karena file telah dibuat atau error telah dihandle
            for(int i=0;i<3;i++) {
                books.writeUTF(bookList[i]);
                books.writeInt(yearList[i]);
            }
            books.seek(0);
            System.out.println(books.readUTF()+" "+books.readInt());
            System.out.println(books.readUTF()+ " "+books.readInt());
            books.close();
        }
        catch(IOException e) {System.out.println("Indeks melebihi batas");} // handling error IO yg terjadi, tidak memberikan notif
        System.out.println("test");
    }
}