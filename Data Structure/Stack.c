#include <stdio.h>
#include <stdlib.h>

struct Stack
{
    int size;
    int top;
    int *arr;
};
int Isempty(struct Stack *ptr){
    if(ptr->top==-1){
        printf("empty\n");
        return 1;
    }
    else{
        printf("not empty\n");
        return 0;
    }
}
int Isfull(struct Stack *ptr){
    if(ptr->top==ptr->size-1){
        printf("full\n");
        return 1;
    }
    else{
        printf("not full\n");
        return 0;
    }    
}
int push(struct Stack*ptr){
    if(Isfull(ptr)==0){
        int a;
        printf("enter element");
        scanf("%d",&a);
        ptr->arr[0]=a;
        ptr->top++;
    }
    else(printf("oops!"));
} 
int pop(struct Stack*ptr){
    if(Isempty(ptr)==0){
        int a;
        a=ptr->arr[ptr->top];
        ptr->top--;
        printf("%d is popped\n",a);

    }
    else(printf("oops!"));
}   

int main()
{
   struct Stack *s;
    s->size = 80;
    s->top = 4;
    s->arr = (int *)malloc(s->size * sizeof(int));
    s->arr[0]=12;
    s->arr[1]=13;
    s->arr[2]=14;
    s->arr[3]=15;
    s->arr[4]=16;
    // Isempty(s);
    // Isfull(s);
    // push(s);
    // int x=s->arr[0];
    // printf("%d\n",x);
    // printf("%d",s->top);
    pop(s);
}
