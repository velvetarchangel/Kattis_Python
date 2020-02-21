//Online Judge problem
//problem# 1172
//Relational Operators in C++
//Author: Himika Dastidar
//Date: 20191130


#include <iostream>

using namespace std;

int main()
{
    int cases, a , b;
    
    std::cin >> cases;
    while(cases --){
        cin >> a >> b;
        if(a > b){
            std::cout << ">" << std::endl;;
        }else if(a < b){
            std::cout<< "<" << std::endl;
        }else{
            std::cout << "=" << std::endl;
        }
    }
    return 0;
}
