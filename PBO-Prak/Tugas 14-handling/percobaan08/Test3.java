// @ubeannn
// 081911633071

package percobaan08;
import java.io.*; // mengimport package "IO" secara keseluruhan

// menganalisa penggunaan "throw" pada program

public class Test3 {
    public void methodA() {System.out.println("Method A");}
    public void methodB() throws IOException { 
        System.out.println(20/0);       // error terjadi dengan tipe "arithmetic '/' by zero '0' "
        System.out.println("Method B");
    }
}

// class Utama { // asal
//     public static void main(String[] args) throws IOException {
//         Test3 c = new Test3();  // membuat objek "Test3" untuk uji code
//         c.methodA(); // menjalankan method A (tidak ada error terjadi)
//         c.methodB(); // menjalankan method B (error terjadi tidak ada handling "try, catch, finally")
//     }
// }

class Utama { // pembenaran program sesuai soal
    public static void main(String[] args) {
        Test3 o = new Test3();  // membuat objek "Test3" untuk uji code
        o.methodA();            // menjalankan method A (tidak ada error terjadi)
        try{o.methodB();}       // menjalankan method B (error terjadi dihandling oleh block "catch")
        catch(Exception e){System.out.println("Error di Method B");} // mencetak pesan karena telah terjadi error
        finally{System.out.println("Ini selalu dicetak");}  // berjalan setelah block "catch" selesai ataupun setelah "try"
    }
}