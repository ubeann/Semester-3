// @ubeannn
// 081911633071

package percobaan03;

// main problem (Arithmetic "/" by zero "0")

// public class Exception03 {
//     public static void main(String[] args) {
//         int bil=10;
//         System.out.println(bil/0);
//     }
// }

// pembenaran (problem solved)

// public class Exception03 { // opsi 1 dengan tipe Exception tidak spesifik
//     public static void main(String[] args) {
//         int bil=10;
//         try {System.out.println(bil/0);}
//         catch(Exception e) {System.out.println("Ini menghandle error yang terjadi");}
//     }
// }

public class Exception03 { // opsi 2 dengan tipe Exception spesifik pada error yg terjadi
    public static void main(String[] args) { 
        int bil=10;
        try {System.out.println(bil/0);}
        // tipe exception pada arithmetic sesuai problem
        catch(ArithmeticException e) {System.out.println("Terjadi Aritmatika error");}
        
        // tipe exception tidak spesifik atau mengacu pada semua problem
        catch(Exception e) {System.out.println("Ini menghandle error yang terjadi");}
    }
}