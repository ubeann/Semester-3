package Percobaan01;

// main problem (index out of bonds)

// public class Exception {
//     public static void main(String[] args) {
//         int a[]=new int[5];
//         a[5]=100;
//     }
// }
    
// pembenaran (problem solved)

public class Exception01 {  
    // nama class perlu dibedakan yg asalnya "Exception" dimana sama dengan Exception type pada syntax "catch"
    // akan menyebabkan error sehingga perlu diganti nama pada file atau public classnya seperti "Exception01"
    public static void main(String[] args) {
        int a[]=new int[5];
        try {a[5]=100;}
        catch(Exception e) {System.out.println("Terjadi pelanggaran memory");}
    }
}