import java.util.*;

public class tri{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();

        if (x == (y + z)) System.out.println(x+"="+y+"+"+z);
        else if (x == (y - z)) System.out.println(x+"="+y+"-"+z);
        else if (x == (y * z)) System.out.println(x+"="+y+"*"+z);
        else if (x == (y / z) && (y%z == 0)) System.out.println(x+"="+y+"/"+z);
        else if ((x + y) == z) System.out.println(x+"+"+y+"="+z);
        else if ((x - y) == z) System.out.println(x+"-"+y+"="+z);
        else if ((x * y) == z) System.out.println(x+"*"+y+"="+z);
        else if ((x / y) == z && (x%y == 0)) System.out.println(x+"/"+y+"="+z);
    }
}