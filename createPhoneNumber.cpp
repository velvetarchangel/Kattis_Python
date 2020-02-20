#include <string>

std::string createPhoneNumber(const int arr [10]){
    char buf[15];
    snprintf(buf, sizeof(buf), "(%d%d%d) %d%d%d-%d%d%d%d\n", arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9]);
    return buf;
  }
