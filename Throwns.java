import java.util.*;
import java.io.*;

public class Throwns{
    public static void main(String[] args) throws Exception{
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String line = sc.readLine();
        String[] line1 = line.split(" ");
        int N = Integer.parseInt(line1[0]);
        int K = Integer.parseInt(line1[1]);
        String line2 = sc.readLine();
        String[] instructions = line2.split(" ");

        Stack<Integer> current_position = new Stack<Integer>();
        current_position.push(0);
        int i = 0;

        while(i < instructions.length){
            if (instructions[i].equals("undo")){
                int temp = Integer.parseInt(instructions[i+1]);
                for(int j = 0; j < temp; j++){
                    current_position.pop();
                    }
                i += 2;
            }else{
                current_position.push(Integer.parseInt(instructions[i]));
                i++;
            }
        }


        int sum = 0;
        for(int j = 0; j < current_position.size(); i++){
            sum += current_position.pop();
        }

        System.out.println(sum % N);
    }
}