#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
    struct Node* prev;
};

void Display(struct Node*ptr){
    while(ptr!=NULL){
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    }
}
struct Node *InsertAtHead(struct Node*head , int data){
    struct Node *ptr = (struct Node*)malloc(sizeof(struct Node));
    head->prev = ptr;
    ptr->data = data;
    ptr->next = head;
    ptr->prev = NULL;
    return ptr;
}
struct Node *InsertAtEnd(struct Node*head , int data){
    struct Node *ptr = (struct Node*)malloc(sizeof(struct Node));
    struct Node *p = head;
    while(p->next!=NULL){
        p=p->next;
    }
    p->next = ptr;
    ptr->prev = p;
    ptr->data = data;
    ptr->next = NULL;
    
}
struct Node* InsertAtIndex(struct Node*head,int data,int index){
    struct Node*ptr = (struct Node*)malloc(sizeof(struct Node));
    struct Node*p = head;
    for(int i=0;i<index-1;i++){
        p=p->next;
    }
    p->next->prev =ptr; 
    ptr->next = p->next;
    p->next=ptr;
    ptr->prev = p;
    ptr->data=data;

}

int main(){
    struct Node* head;
    struct Node* second;
    struct Node* third;
    struct Node* fourth;

    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    fourth=(struct Node*)malloc(sizeof(struct Node));

    head->data=10;
    head->next=second;
    head->prev=NULL;

    second->data=20;
    second->next=third;
    second->prev=head;

    third->data=30;
    third->next=fourth;
    third->prev=second;

    fourth->data=40;
    fourth->next=NULL;
    fourth->prev=third;

Display(head);
head = InsertAtHead(head,0);
Display(head);
printf("\n");
InsertAtEnd(head,50);
Display(head);
InsertAtIndex(head,-100,3);
Display(head);
}