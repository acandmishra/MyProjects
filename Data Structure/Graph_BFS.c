#include <stdio.h>
#include <stdlib.h>
// very important program!!
// Queue is taken from prev program and is modified a little!!

struct Queue{
    int size;
    int top;
    int *arr;
};

int Isempty(struct Queue*ptr){
    if(ptr->top==-1){
        
        return 1;
    }
    else{
        
        return 0;
    }
}
int Isfull(struct Queue*ptr){
    if(ptr->top==ptr->size-1){
        
        return 1;
    }
    else{
        
        return 0;
    }
}
int push(struct Queue*ptr,int a){
    if(Isfull(ptr)==1){
        printf("Overqueued\n");
    }
    else{
        for(int i=0,j=ptr->top;i<=ptr->top;j--,i++){
            ptr->arr[j+1]=ptr->arr[j];
        }
        ptr->arr[0]=a;
        ptr->top++;
    }
}
int pop(struct Queue*ptr){
    if(Isempty(ptr)==1){
        printf("Underqueued\n");
    }
    else{
    int a;
    a=ptr->arr[ptr->top];
    ptr->top--;
    
    return a;
    }

}
void display(struct Queue *ptr){
    for(int i=0;i<=ptr->top;i++){
        printf("%d\n",ptr->arr[i]);
    }
}

int main(){
    struct Queue *q;
    q->size = 10;
    q->arr = (int*)malloc(q->size*sizeof(int));
    q->top = -1;
    int node;
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
    int i = 0; // starting location
    push(q,i); // inserting the starting location into the exploration queue
    visited[i] = 1; // labelling the starting location as true(1)
    printf("%d\n",i);
    while(!Isempty(q)){
        int node = pop(q);
        for(int j = 0;j<7;j++){
            if(Graph[node][j]==1 && visited[j]==0){
                printf("%d\n",j);
                visited[j] = 1;
                push(q,j);

            }
        }    
    }
   return 0;
    
}