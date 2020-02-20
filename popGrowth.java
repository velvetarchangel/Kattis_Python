class popGrowth{
    
    public static int nbYear(int p0, double percent, int aug, int p) {
        int population = p0;
        int year = 0;
        
        while (population < p){
          int growth = (int)((population * percent*0.01) + aug);
          population += growth;
          year ++;
          growth = 0;
        }
        return year;
    }
}
