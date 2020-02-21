//Problem from Online Judge
//Problem name: Division of Nlognia
//Nov 30, 2019
// Author: Himika Dastidar

#include <iostream>

using namespace std;

int main()
{
    int cases, x , y, div_x, div_y;
    
    std::cin >> cases;
    while(cases != 0){
        std::cin >> div_x >> div_y;
        
        while(cases --){
            cin >> x >> y;
            if (x == div_x || y == div_y){
                std::cout << "divisa" << std::endl;
            }else if(x > div_x && y > div_y){
                std::cout << "NE" << std::endl;;
            }else if(x < div_x && y < div_y){
                std::cout<< "SO" << std::endl;
            }else if (x > div_x && y < div_y){
                std::cout << "SE" << std::endl;
            }else if (x < div_x && y > div_y){
                std::cout << "NO" << std::endl;
            }
        }
    }
    return 0;
}
