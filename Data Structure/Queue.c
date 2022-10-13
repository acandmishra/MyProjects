#include <stdio.h>
#include <stdlib.h>

struct Queue{
    int size;
    int top;
    int *arr;
};

int Isempty(struct Queue*ptr){
    if(ptr->top==-1){
        printf("queue is empty\n");
        return 1;
    }
    else{
        printf("queue is not empty\n");
        return 0;
    }
}
int Isfull(struct Queue*ptr){
    if(ptr->top==ptr->size-1){
        printf("queue is full\n");
        return 1;
    }
    else{
        printf("queue is not full\n");
        return 0;
    }
}
int push(struct Queue*ptr){
    if(Isfull(ptr)==1){
        printf("Overqueued\n");
    }
    else{
        int a;
        printf("enter the element:");
        scanf("%d",&a);
        for(int i=0,j=ptr->top;i<=ptr->top;j--,i++){
            ptr->arr[j+1]=ptr->arr[j];
        }
        ptr->arr[0]=a;
        ptr->top++;
    }
}
int pop(struct Queue*ptr){
    int a;
    a=ptr->arr[ptr->top];
    ptr->top--;
    printf("the popped element is %d\n",a);

}
void display(struct Queue *ptr){
    for(int i=0;i<=ptr->top;i++){
        printf("%d\n",ptr->arr[i]);
    }
}

int main(){
    struct Queue *q;
    q->size = 10;
    q->top = 4;
    q->arr = (int*)malloc(q->size*sizeof(int));
    q->arr[0]=5;
    q->arr[1]=4;
    q->arr[2]=3;
    q->arr[3]=2;
    q->arr[4]=1;
    display(q);
    push(q);
    display(q);
    printf("the top element is:%d\n",q->top);
    pop(q);
    display(q);
    return 0;
    
}