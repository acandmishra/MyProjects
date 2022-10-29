#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

void Display(struct Node*head){
    struct Node*ptr=head;
    while(ptr!=NULL){
        printf("%d\n",ptr->data);
        ptr=ptr->next;
    }
}

struct Node* Push(struct Node*head,int data){
    struct Node* p = head;
    struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
    while(p->next!=NULL){
        p=p->next;
    }
    ptr->data=data;
    p->next = ptr;
    ptr->next=NULL;
}
struct Node* Pop(struct Node*head){
    struct Node*ptr = head;
    while(ptr->next->next!=NULL){
        ptr = ptr->next;
    }
    printf("popped element is:%d\n",ptr->next->data);
    free(ptr->next);
    ptr->next=NULL;

}

int main(){
    struct Node*head = (struct Node*)malloc(sizeof(struct Node));
    struct Node*second = (struct Node*)malloc(sizeof(struct Node));
    struct Node*third = (struct Node*)malloc(sizeof(struct Node));
    struct Node*fourth = (struct Node*)malloc(sizeof(struct Node));

    head->next = second;
    head->data = 10;

    second->next = third;
    second->data = 20;

    third->next = fourth;
    third->data = 30;

    fourth->next = NULL;
    fourth->data = 40;
Display(head);
Push(head,50);
printf("\n");
Display(head);
Pop(head);
Display(head);
}