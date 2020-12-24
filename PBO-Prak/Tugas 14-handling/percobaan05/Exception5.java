// @ubeannn
// 081911633071

package percobaan05;

// menganalisa penggunaan "try" & "catch" untuk handling error yang terjadi

public class Exception5 {
    public static void main(String[] args) {
        int bil=10;
        try{System.out.println(bil/0);}             // terjadi error arithmetic '/' by zero '0'
        catch(ArithmeticException e) {              // menangkapan exception atau error secara spesifik "ArithmeticException"
            System.out.println("Pesan error: ");
            System.out.println(e.getMessage());     // memberikan penjelasan mengapa error terjadi
            System.out.println("Info stack erase");
            e.printStackTrace();                    // mencetak stack trace pada error yang terjadi
            e.printStackTrace(System.out);          // sama mencetak stack trace pada error yang terjadi
        }

        // menangkap exception tidak spesifik
        // tidak di run oleh program disebabkan error spesifik akan diprioritaskan terlebih dahulu
        catch(Exception e){System.out.println("Ini menghandle error yang terjadi");}
    }
}