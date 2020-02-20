#include<string>
using namespace std;
class CountDig
{
public:
    static int nbDig(int n, int d);
};


int CountDig::nbDig(int n, int d){
  int count = !d;
  for(int i = 0; i <= n; ++i){
    for(int m = i*i; m; m/= 10){
      count += m % 10 == d;
      }
    }
    
    return count;
  }
