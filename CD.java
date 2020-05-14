import java.util.*;
import java.io.*;

public class CD{

    public static void main(String[] args)throws Exception {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String line = sc.readLine();
        String[] CDowned = line.split(" ");

        int N = Integer.parseInt(CDowned[0]); //Jack
        int M = Integer.parseInt(CDowned[1]); //Jill

        HashSet<String> jack = new HashSet<String>();

        while (true) {
            if (N == 0 && M == 0) {
                break;
            } else {
                for (int i = 0; i < N; i++) {
                    String temp = sc.readLine();
                    jack.add(temp);
                }

                int commonCD = 0;

                for (int i = 0; i < M; i++) {
                    String temp = sc.readLine();
                    if (jack.contains(temp)) {
                        commonCD++;
                    }
                }
                System.out.println(commonCD);
            }

            line = sc.readLine();
            CDowned = line.split(" ");
            N = Integer.parseInt(CDowned[0]);
            M = Integer.parseInt(CDowned[1]);
            jack.clear();
        }
    }
}