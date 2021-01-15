// By @Ubean 081911633071
package nomor3;

public class ArithmeticExceptionHandle {
    public static void main(String[] args) {
        final int number1 = 71;
        final int number2 = 0;
        try{int output = number1/number2;}          // Making ArithmeticException (divide by zero)
        catch(ArithmeticException e){
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("ArithmeticException is handled.");
        }
    }
}
