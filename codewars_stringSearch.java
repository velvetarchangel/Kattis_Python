import java.util.regex.*;

public class SearchEngine {
    static int find(String needle, String haystack){
    
        String regneedle = "\\Q" + needle.replaceAll("_", "\\\\E.\\\\Q") +"\\E";
        Matcher m = Pattern.compile(regneedle).matcher(haystack);
        if(m.find()) return m.start();
        else return -1;
    }
}
