// By @Ubean 081911633071
package nomor3;

public class StringIndexOutOfBoundsExceptionHandle {
    public static void main(String[] args) {
        try{                                            // Making StringIndexOutOfBoundsException
            String text = "ubean here";                 // The index is either negative or greater than the size of the string.
            System.out.println(text.charAt(71));
        }
        catch(StringIndexOutOfBoundsException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("StringIndexOutOfBoundsException is handled.");
        }
    }
}
