import java.util.*;
import java.io.*;

public class geneticSearch{

    public static int Type1(String S, String L){
        int count = 0;
        for(int i = 0; i < L.length()-S.length()+1; i++){
            if(L.substring(i, i+S.length()).equals(S)) count++;
        }

        return count;
    }

    public static int Type2(String S, String L){
        Set<String> setOfStrings = new HashSet<>();
        int count = 0;
        for(int i = 0; i < S.length(); i++){
            String t = S.substring(0,i) + S.substring(i+1,S.length());
            if(!setOfStrings.contains(t)) {
                setOfStrings.add(t);
                count += Type1(t, L);
            }
        }
        return count;
    }

    public static int Type3(String S, String L){
        Set<String> setOfStrings = new HashSet<>();
        int count = 0;
        String[] arr = {"A","T","C","G"};
        Set<String> str = new HashSet<>();

        for(int j = 0; j < arr.length; j++){
            for(int i = 0; i < S.length() + 1; i++){
                String temp = S.substring(0,i) + arr[j] + S.substring(i, S.length());
                if(!str.contains(temp)){
                    str.add(temp);
                    count += Type1(temp, L);
                }
            }
        }
        return count;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            String[] input = sc.readLine().split(" ");
            if(input[0].equals("0")) break;
            String S = input[0];
            String L = input[1];
            int type1 = Type1(S, L);
            int type2 = Type2(S, L);
            int type3 = Type3(S, L);

            System.out.println(type1 +" " + type2 + " " + type3);

        }
        
    }
}