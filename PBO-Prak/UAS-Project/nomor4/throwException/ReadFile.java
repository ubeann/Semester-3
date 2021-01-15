// By @Ubean 081911633071
package nomor4.throwException;

// import modules from "Java.io"
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
// import exceptions for handling error
import java.io.FileNotFoundException;
import java.io.IOException;

// main problem (Using Solution 2)
public class ReadFile {
    // give "throws" keyword for Exceptions List to handling error in code
    public static void main(String args[]) throws FileNotFoundException, IOException{ 
        File file = new File("Data.txt"); 
        BufferedReader fileReader;
        fileReader = new BufferedReader(new FileReader(file));
        while(true){
            String line = fileReader.readLine(); 
            if (line == null) break ; 
            System.out.println(line);
        }
    }
}