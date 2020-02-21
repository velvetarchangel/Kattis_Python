import java.util.*;

public class diceCup{
    //Method to return index of the element with the max value
    public static int returnMaxIndex(int[] arr){
        int maxIndex = 0;
        for (int i = 0; i < arr.length; i ++){
            if (arr[i] > arr[maxIndex]){
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num_die = sc.nextInt();
        int faces = sc.nextInt();

        int[] count = new int[num_die + faces + 1];

        /*populate the count array so each index refers 
        to the number of time something is being rolled*/
        for (int i = 1; i <= num_die; i++){
            for (int j = 1; j <= faces; j++){
                count[i+j] ++;
            }
        }

        int maxIndex = returnMaxIndex(count);
        
        for(int i = 0; i < count.length; i++){
            if (count[i] == count[maxIndex]) System.out.println(i);
        }
        
    }
}