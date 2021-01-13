// By @Ubean 081911633071
package nomor3;

public class NegativeArraySizeExceptionHandle {
    public static void main(String[] args) {
        try{                                            // Making NegativeArraySizeException
            Object[] ubean = new String[-71];           // tries to create an array with negative size.
            System.out.println(ubean[71]);
        }
        catch(NegativeArraySizeException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("NegativeArraySizeException is handled.");
        }
    }
}
