// By @Ubean 081911633071
package nomor3;

public class ArrayStoreExceptionHandle {
    public static void main(String[] args) {
        try{                                    // Making ArrayStoreException 
            Number[] array = new Double[1];     // (mismatch to store a value in an array)
            array[0] = 71;
        }
        catch(ArrayStoreException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("ArrayStoreException is handled.");
        }
    }
}
