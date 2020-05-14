import java.util.*;
import java.io.*;

public class evenUp{

    public static void main(String[] args) throws Exception{

        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String line = sc.readLine();
        int n = Integer.parseInt(line);
        String line2 = sc.readLine();
        String[] s = line2.split(" ");

        Stack<Integer> numbers = new Stack<Integer>();
        Stack<Integer> sparePile = new Stack<Integer>();

        for (int i = 0; i < s.length; i++){
            numbers.add(Integer.parseInt(s[i]));
        }

        while(numbers.size() > 0){
            int last_item = numbers.pop();
            sparePile.push(last_item);
            
            while(numbers.size() > 0 && sparePile.size() > 0 && ((sparePile.peek() + numbers.peek())%2 == 0)){
                sparePile.pop();
                numbers.pop();
            }
        }

        System.out.println(sparePile.size());
    }
}