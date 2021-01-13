// By @Ubean 081911633071
package nomor3;

public class NullPointerExceptionHandle {
    public static void main(String[] args) {
        try{                                            // Making NullPointerException
            Object[] ubean = new String[71];            // attempts to use null in a case where an object is required
            ubean[0].equals(null);
        }
        catch(NullPointerException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("NullPointerException is handled.");
        }
    }
}
