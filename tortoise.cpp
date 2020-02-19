class Tortoise
{
public:
    static std::vector<int> race(int v1, int v2, int g);
};

std::vector<int> Tortoise::race(int v1, int v2, int g){
  if(v1 >= v2) return {-1, -1, -1};
    int time = g*3600/(v2-v1);
    
    return {time/3600, time / 60 % 60,time % 60};

  }
