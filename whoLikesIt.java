import java.util.*;

class whoLikesIt {
    public static String whoLikesIt(String... names) {
        StringBuilder who = new StringBuilder();
        if (names.length == 0) who.append("no one likes this");
        else if (names.length == 1) who.append(names[0] + " likes this");
        else if (names.length == 2) who.append(names[0] + " and " + names[1] + " like this");
        else if (names.length == 3) who.append(names[0] + ", " + names[1] + " and " + names[2] + " like this");
        else who.append(names[0] + ", " + names[1] + " and " + Integer.toString(names.length-2) + " others like this");
        return who.toString();
    }
}
