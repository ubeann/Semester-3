// By @Ubean 081911633071
package nomor5.modules;
public class Stack{
    // size : menentukan besar array untuk menyimpan data. Array berdimensi satu dengan tipe Object.
    private int size;

    // top : merupakan tanda indeks yang paling atas, yang belum terisi. 
    // Sehingga data yang akan masuk akan dimasukkan pada indeks tersebut.
    private int top;

    // Object[] elemen : untuk menyimpan data.
    private Object[] elemen;

    //  jika kita membuat object Stack dengan konstruktor Stack() maka tentukan size = 5
    public Stack(){
        this.size = 5;
        this.elemen = new Object[5];
        this.top = 0;
    }
    
    // jika kita membuat object Stack dengan konstruktor Stack(int s) maka tentukan size berdasarkan parameter s
    public Stack(int size){
        this.size = size;
        this.elemen = new Object[size];
        this.top = 0;
    }

    // getSize() untuk mendapatkan besar array dari Stack
    public int getSize(){return this.size;}

    // getTop() untuk mendapatkan top dari Stack
    public int getTop(){return this.top;}
    
    // push(Object o) untuk memasukkan data ke array pada Stack.
    public void push(Object o){
        if (this.top < this.size) this.elemen[this.top] = o;
        else throw new FullStackException("Stack telah full");
        this.top++;
    }

    // pop() untuk mengambil data dari array
    public Object pop(){
        this.top--;
        if (this.top >=0 ) return this.elemen[this.top];
        else {
            this.top = 0;
            throw new EmptyStackException("Stack Kosong!");
        }
    }
}