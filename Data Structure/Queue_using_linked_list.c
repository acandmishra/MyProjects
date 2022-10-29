#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node*next;
};

void Display(struct Node*head){
    struct Node*p = head;
    while(p!=NULL){
        printf("%d\n",p->data);
        p=p->next;

    }
}

struct Node* Push(struct Node* head,int data){
    struct Node*ptr = (struct Node*)malloc(sizeof(struct Node));
    struct Node*p = head;
    while(p->next!=NULL){
        p=p->next;
    }
    p->next=ptr;
    ptr->data=data;
    ptr->next=NULL;
}

struct Node*Pop(struct Node*head){
    struct Node*p = head;
    head = p->next;
    printf("element popped is:%d",p->data);
    free(p);
    return head;
}

int main(){
    struct Node*head = (struct Node*)malloc(sizeof(struct Node));
    struct Node*second = (struct Node*)malloc(sizeof(struct Node));
    struct Node*third = (struct Node*)malloc(sizeof(struct Node));
    struct Node*fourth = (struct Node*)malloc(sizeof(struct Node));


    head->data = 10;
    head->next = second;

    second->data = 20;
    second->next = third;

    third->data = 30;
    third->next = fourth;

    fourth->data = 40;
    fourth->next = NULL;
    
    Display(head);
    Push(head,50);
    printf("\n");
    Display(head);
    head = Pop(head);
    printf("\n");
    Display(head);
}
