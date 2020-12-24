// @ubeannn
// 081911633071

package percobaan09;

// menjalankan program atau method "String reverse()"

class Propagate {
    public static void main(String[] args) {
        // try {System.out.println(reverse("This is a string"));}   // program berjalan lancar tanpa kendala
        try {System.out.println(reverse(""));}                      // mengganti dengan parameter "" sesuai permintaan soal
        catch(Exception e) {System.out.println("The String was blank");}    // handling apabila error terjadi, memberikan notif
        finally {System.out.println("All done");}   // akan selalu berjalan meskipun "error" terjadi ataupun "tidak"
    }
    public static String reverse(String s) throws Exception {
        if(s.length() == 0) {throw new Exception();}    // apabila kondisi "true" maka "throw" Exception atau error
        String reverseStr = "";
        for(int i=s.length()-1 ; i >= 0 ; --i) {reverseStr += s.charAt(i);}
        return reverseStr;
    }
}