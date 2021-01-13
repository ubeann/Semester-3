// By @Ubean 081911633071
package nomor3;

public class ClassCastExceptionHandle {
    public static void main(String[] args) {
        try{                                    // Making ClassCastException
            Object ubean = new Double(71);          // attempted to cast an object to a subclass of which it is not an instance
            System.out.println((char)ubean);
        }
        catch(ClassCastException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("ClassCastException is handled.");
        }
    }
}