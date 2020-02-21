//Fails on case 26/72 in Kattis unknown why
//Date 20191214
//Author: Himika Dastidar
//Source: Kattis
//Problem: Tais Formula

#include <iostream>
#include <iomanip>
using namespace std;
#include <string>
#include <array>

int main()
{
  int N;
  float t, g;
  float glucose_reading = 0.0;
  std::cin >> N;
  float array[N][2];
  
    for (int i = 0; i < N; i ++){
      std::cin >> t >> g;
      array[i][0] = t;
      array[i][1] = g;
    }
    
    for (int i = 0; i < N-1; i ++){
        glucose_reading += (((array[i][1] + array[i+1][1])/2) * (array[i+1][0]-array[i][0])/1000);
    }
    
    cout << fixed;
    cout.precision(6);
    std::cout << glucose_reading <<std::endl;

}
