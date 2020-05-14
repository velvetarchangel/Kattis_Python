import java.util.*;
import java.io.*;

public class pairingSocks{

    public static void main(String[] args) throws Exception{

        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String line = sc.readLine();
        int targetPair = Integer.parseInt(line);
        String line2 = sc.readLine();
        String[] s = line2.split(" ");

        Stack<Integer> socks = new Stack<Integer>();    //Initial pile
        Stack<Integer> auxPile = new Stack<Integer>();

        for(int i = 0; i < s.length; i++){
            socks.push(Integer.parseInt(s[i]));
        }

        int moves = 0;

        while(socks.size() != 0){
            auxPile.push(socks.pop());
            moves++;
            if(socks.size() > 0 && auxPile.size() > 0 && auxPile.peek() == socks.peek()){
                moves++;
                auxPile.pop();
                socks.pop();
            }
        }

        if(auxPile.size() != 0) System.out.println("impossible");
        else System.out.println(moves);
    }
}