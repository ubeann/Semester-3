// By @Ubean 081911633071
package nomor3;

public class NumberFormatExceptionHandle {
    public static void main(String[] args) {
        try{                                        // Making NumberFormatException
            int ubean = Integer.parseInt(null);     // attempted to convert a string to one of the numeric types, 
            System.out.print(ubean);                // but that the string does not have the appropriate format.
        }
        catch(NumberFormatException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("NumberFormatException is handled.");
        }
    }
}
