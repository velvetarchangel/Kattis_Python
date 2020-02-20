using namespace std;
class Bouncingball
{
public:
    static int bouncingBall(double h, double bounce, double window);
  };


int Bouncingball::bouncingBall(double h, double bounce, double window){
  int down = 1;
  int up = 0;
      if (h < 0 || bounce <= 0 || bounce >= 1 || window >= h) {
        return -1;
      }else{
      h *= bounce;
        while(h > window){
          up ++;
          down ++;
          h *= bounce;
          }
        }
        return up + down;
        }
