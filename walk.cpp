#include<vector>

bool isValidWalk(std::vector<char> walk) {
  int time = 0;
  int count_n = 0;
  int count_s = 0;
  int count_e = 0;
  int count_w = 0;
  
  for (int i = 0; i < walk.size(); i++){
    if (walk[i] == 'n') count_n++;
    else if (walk[i] == 's') count_s++;
    else if (walk[i] == 'e') count_e++;
    else count_w++;
    }
    
    time = count_n + count_s + count_e + count_w;
    
    if ((time == 10) && (count_n == count_s) && (count_e == count_w)) return true;
    else return false;
}
