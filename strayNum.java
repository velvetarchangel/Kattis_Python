import java.util.*;
class Solution {
  static int stray(int[] numbers) {
    int num_one = numbers[0];
    int num_two = 0;
    int count_one = 1;
    int count_two = 0;
    
    for(int i = 1; i < numbers.length; i ++){
      if (numbers[i] == num_one) count_one ++;
      else num_two = numbers[i]; count_two ++;
      }
    
    if (count_one == 1) return num_one;
    else return num_two;
  }
}
