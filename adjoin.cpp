// Adjoin the Networks

#include <iostream>
#include <vector>
using namespace std;

class Edge{
    public:
        Edge(Vertex *start, Vertex *end)
        {
            start = start;
            end = end;
        }

    };

class Vertex{
    public:
    Vertex(int id){
        id = id;
    }

    void addEdge(Vertex *other){
        Edge newEdge(this, other);
    }
};

class Graph{
    public:
    Graph(){

    }

};

int main()
{
    int c, l;
    int a, b;

    std::cin>> c >> l;
    while(l--){
        std::cin>> a >> b;
    }
    
}