// By @Ubean 081911633071
package nomor3;

import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class NoSuchElementExceptionHandle {
    public static void main(String[] args) {
        try{                                            // Making NoSuchElementException
            String str = "Hi Ubeann";                   // element being requested does not exist.
            // Instantiating the StringTokenizer class
            StringTokenizer ubean = new StringTokenizer(str, " ");
            // Printing all the tokens (include doesn't exist)
            System.out.println(ubean.nextToken());
            System.out.println(ubean.nextToken());
            System.out.println(ubean.nextToken());
        }
        catch(NoSuchElementException e){
            System.out.println("------------------");
            System.out.println("Handle Error:");
            e.printStackTrace();
            System.out.println("We are just printing the stack trace.");
            System.out.println("NoSuchElementException is handled.");
        }
    }
}
