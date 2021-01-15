// By @Ubean 081911633071
package nomor4.catchException;

// import modules from "Java.io"
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
// import exceptions for handling error
import java.io.FileNotFoundException;
import java.io.IOException;

// main problem (Using Solution 1)
public class ReadFile {
    public static void main(String args[]){ 
        File file = new File("Data.txt"); 
        BufferedReader fileReader;
        try{                                                            // giving code block "try"
            fileReader = new BufferedReader(new FileReader(file));
            while(true){
                String line = fileReader.readLine(); 
                if (line == null) break ; 
                System.out.println(line);
            }
        }
        catch(FileNotFoundException e){                                 // "catch" block for FileNotFoundException (subclass "IOException")
            System.out.println("-> Handling FileNotFoundException");
            System.out.println(e.toString());
        }
        catch(IOException e){                                           // "catch" block for IOException
            System.out.println("-> Handling IOException");
            System.out.println(e.toString());
        }
    }
}