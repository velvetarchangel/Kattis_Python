import java.util.*;

public class createPhoneNumber {

  public static String createPhoneNumber(int[] numbers) {
    StringBuilder s = new StringBuilder("");
    s.append("(");
    for (int i = 0; i < 3; i++){
      s.append(numbers[i]);
      }
    s.append(") ");
    for (int i = 3; i < 6; i++){
      s.append(numbers[i]);
      }
    s.append("-");
    for(int i = 6; i < 10; i++){
      s.append(numbers[i]);
      }
    return s.toString();
  }
}
