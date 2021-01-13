// By @Ubean 081911633071
package nomor3;

public class ArrayIndexOutOfBoundsExceptionHandle {
    public static void main(String[] args) {
        try{                                            // Making ArrayIndexOutOfBoundsException
            Object[] ubean = new String[71];            // The index is either negative or greater than or equal to the size of the array.
            System.out.println(ubean[72]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("ArrayIndexOutOfBoundsException is handled.");
        }
    }
}
