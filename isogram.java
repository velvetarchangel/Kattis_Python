import java.util.*;

public class isogram {
    public static boolean  isIsogram(String str) {
        String str_lower = str.toLowerCase();
        HashSet<Character> isogram = new HashSet<Character>();
        for (int i = 0; i < str_lower.length(); i ++) isogram.add(str_lower.charAt(i));
        if (isogram.size() == str.length()) return true;
        else return false;
        
    } 
}
