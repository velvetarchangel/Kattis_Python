import java.util.*;

public class MorseCodeDecoder {
    public static String decode(String morseCode) {
        StringBuilder s = new StringBuilder("");
        String[] coded = morseCode.trim().split("   ");
        
        
        for (int j = 0; j < coded.length; j++){
        
          String[] letters = coded[j].split(" ");
          
          for(int i = 0; i < letters.length; i++){
            if(MorseCode.get(letters[i])!= null) s.append(MorseCode.get(letters[i]));
            }
          s.append(" ");
          }
        s.deleteCharAt(s.length()-1);

        return s.toString();
    }
}
