// @ubeannn
// 081911633071

package percobaan06;

// menganalisa penggunaan "try" & "catch" untuk handling error yang terjadi

public class ThrowExample {
    static void demo() {
        NullPointerException t;                     // inisiasi objek error dengan tipe "NullPointerException"
        t = new NullPointerException("Coba Throw"); // membuat objek error dengan tipe "NullPointerException" dengn pesan tertera
        throw t;                                    // melempar exception atau error yang telah dibuat pada objek 't'
        // Baris ini tidak lagi dikerjakan;
        // System.out.println("Ini tidak lagi dicetak"); // merupakan "Unreachable code"
    }
    public static void main(String[] args) {
        try {
            demo();
            System.out.println("Selesai"); // juga merupakan "Unreachable code" dikarenakan error yang terjadi
        }
        // menangkap error NullPointerException serta memberikan notifikasi atau pesan sesuai error yang terjadi
        catch(NullPointerException e) {System.out.println("Ada pesan error: "+e);} 
    }
}