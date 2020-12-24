// @ubeannn
// 081911633071

package percobaan02;

// main problem (array index out of bonds)

// public class Exception02 {
//     public static void main(String[] args) {
//         int i=0;
//         String greeting[]={
//             "Hello World!",
//             "No, I mean it!",
//             "Hello World"
//         };
//         while(i<4) {
//             System.out.println(greeting[i]);
//             i++;
//         }
//     }
// }

// pembenaran (problem solved)

public class Exception02 {
    public static void main(String[] args) {
        int i=0;
        String greetings[]={
            "Hello World!",
            "No,I mean it!",
            "HELLO WORLD!"
        };
        while(i<4) {
            try {
                System.out.println(greetings[i]);
                i++;
            }
            catch(ArrayIndexOutOfBoundsException e) {
                System.out.println("Resetting index value");
                i=0;    // infinite looping disebabkan variabel terminasi diriset
            }
        }
    }
}