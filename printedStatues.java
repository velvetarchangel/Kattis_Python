import java.util.*;

class printedStatues{
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        double statues = sc.nextInt();
        int printers = 1;
        int days = 0;
        if(statues == 1){
            System.out.println(1);
        }else {
            while (printers < Math.ceil(statues/2)) {
                printers *= 2;
                days++;
            }
            System.out.println(days + 2);
        }
    }
}