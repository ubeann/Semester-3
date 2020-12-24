// @ubeannn
// 081911633071

package percobaan11;

// menunjukkan proses throw and catch pada class yang extends Throwable

class RangeErrorException extends Throwable { // class yg inherit atau memiliki parent "Throwable"
    public RangeErrorException(String s) {super(s);} // membuat konstruktor dengan super atau parent "Throwable"
    public static void main(String[] args) {
        int position=1;

        // apabila kondisi if "true" maka throw error sesuai objek yg telah dibuat sesuai class ini (ikut konstruktor)
        try {if(position>0) throw new RangeErrorException("Position " +position);} 

        // handling error yg terjadi, memberikan notif serta penjelasan error yg terjadi
        catch(RangeErrorException e) {System.out.println("Range error: " +e.getMessage());}
        
        System.out.println("This is the last program.");
    }
}