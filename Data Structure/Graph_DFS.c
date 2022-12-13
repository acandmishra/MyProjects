#include<stdio.h>

int visited[7] = {0,0,0,0,0,0,0}; // to check for visit status ,0->not visited , 1->visited
    int Graph[7][7] = {   // graph adjacency matrix representation
        {0,1,0,1,0,0,0},
        {1,0,0,1,0,0,0},
        {0,0,0,0,1,0,0},
        {1,1,0,0,0,1,0},
        {0,0,1,0,0,0,1},
        {0,0,0,1,1,0,0},
        {0,0,0,0,1,0,0}     // Answer should be 0135426
    }; 

void DFS(int node){ // node is the starting
    printf("%d",node);
    visited[node]=1;
    for (int j = 0; j < 7; j++)
    {
        if(Graph[node][j]==1 && visited[j]==0){
            DFS(j);
        }
    }
    
}
int main(){
    DFS(0);
    return 0;

}