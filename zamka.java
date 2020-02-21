import java.util.*;

public class zamka{
    /**finds the maximal integer M where the sum
     * of the digits is equal to X */
    public static int findM(int L, int D, int X){
        int max = -1000;

        for (int i = D; i >= L; i--){
            int intermediate = i;
            int sum_digits = 0;

            while(intermediate != 0){
                sum_digits += intermediate % 10;
                intermediate /= 10;
            }

            if (sum_digits == X){
                max = i;
                break;
            }
        }
        return max;
    }

    /**finds the minimal integer N where the sum
     * of the digits is equal to X */
    public static int findN(int L, int D, int X){

        int min = 1000;

        for (int i = L; i <=D; i++){
            int intermediate = i;
            int sum_digits = 0;

            while(intermediate != 0){
                sum_digits += intermediate % 10;
                intermediate /= 10;
            }

            if (sum_digits == X){
                min = i;
                break;
            }
        }
        return min;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        int D = sc.nextInt();
        int X = sc.nextInt();

        System.out.println(findN(L, D, X));
        System.out.println(findM(L, D, X));

    }
}