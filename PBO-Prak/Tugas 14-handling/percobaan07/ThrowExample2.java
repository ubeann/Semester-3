// @ubeannn
// 081911633071

package percobaan07;

// menganalisa penggunaan "try" & "catch" untuk handling error yang terjadi

public class ThrowExample2 {
    public static void main(String[] args) {
        try {throw new Exception("Here's my Exception");}   // membuat dan mengirim objek error dengan pesan yg tertera
        catch(Exception e) {    // menangkap error yg terjadi pada block syntax "try"
            System.out.println("Caught Exception");
            System.out.println("e.getMessage():"+e.getMessage());   // mencetak pesan atau notifikasi error yg terjadi
            System.out.println("e.toString():"+e.toString());       // mencetak error dengan method toString()
            System.out.println("e.printStackTrace():"); 
            e.printStackTrace();                                    // mencetak StackTrace error yg telah terjadi
        }
    }
}