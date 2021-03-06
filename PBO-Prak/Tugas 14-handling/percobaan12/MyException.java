// @ubeannn
// 081911633071

package percobaan12;

// menunjukkan proses throw and catch pada class yang extends "Exception"

class MyException extends Exception{ // class yg inherit atau memiliki parent "Exception"
    private String Teks;
    MyException(String s) {
        Teks="Exception generated by: "+s;
        System.out.println(Teks);
    }
}

class Eksepsi {
    static void tampil(String s) throws Exception {
        System.out.println("Tampil");

        // jika kondisi "true" maka throw error atau Exception yg telah dibuat
        if(s.equals("amir")) throw new MyException(s); 

        System.out.println("OK!"); // akan dirun apabila tidak terjadi error
    }
    public static void main(String[] args) throws Exception {
        try {
            tampil("ali");
            tampil("amir");
        }
        catch(MyException ex) {System.out.println("Tangkap:"+ex);} // handling error yg terjadi, memberikan notif penjelasan
    }
}