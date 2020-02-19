import java.util.ArrayList;

class Metro {

  public static int countPassengers(ArrayList<int[]> stops) {
  
    int number_on = 0;
    int number_off = 0;
    
    for(int i = 0; i < stops.size(); i++){
      int[] passengers = stops.get(i);
      number_on += passengers[0];
      number_off += passengers[1];
    }
    
    return number_on-number_off;
  }
}
