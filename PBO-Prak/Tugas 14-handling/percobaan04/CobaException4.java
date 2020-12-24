// @ubeannn
// 081911633071

package percobaan04;

// main problem (terdapat 2 error type pada 1 block syntax "try & catch")

// public class CobaException4 {
//     public static void main(String[] args) {
//         int bil=10;
//         String b[]={"a","b","c"};
//         try {
//             System.out.println(b[3]);    // error array index out of bonds (exception hanya menghandel error ini, program stopped)
//             System.out.println(bil/0);   // error arithmetic "/" by zero "0"
//         }
//         catch(ArithmeticException e) {System.out.println("Terjadi Aritmatika error");}
//         catch(ArrayIndexOutOfBoundsException e) {System.out.println("Melebihi jumlah array");}
//         catch(Exception e) {System.out.println("Ini menghandle error yang terjadi");}
//     }
// }
    
// pembenaran (meski tidak dapat dibilang fixed code)

public class CobaException4 { // masih terdapat 2 error type pada 1 block syntax "try & catch"
    public static void main(String[] args) {
        int bil=10;
        String b[]={"a","b","c"};
        try {
            System.out.println(bil/0);  // error arithmetic "/" by zero "0" (exception hanya menghandel error ini, program stopped)
            System.out.println(b[3]);   // error array index out of bonds
        }
        catch(ArithmeticException e) {System.out.println("Terjadi Aritmatika error");}
        catch(ArrayIndexOutOfBoundsException e) {System.out.println("Melebihi jumlah array");}
        catch(Exception e){System.out.println("Ini menghandle error yang terjadi");}
    }
}    