#include <stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node* next;
};

void Display(struct Node*ptr){
    while(ptr!=NULL){
        printf("Element:%d\n",ptr->data);
        ptr=ptr->next;
    } 
}
struct Node* deletioninbetween(struct Node* head,int node){
    struct Node * ptr=head;
    struct Node * pptr= ptr->next;
    int i=0;
    while(i!=(node-1)){
    ptr=ptr->next;
    pptr=pptr->next;
    i++;
    }
    ptr->next=pptr->next;
    free(pptr);
    
    return head;
}
struct Node * deletionatnode(struct Node * head,struct Node* ptr){
    struct Node * pptr = head;
    struct Node * ppptr=head->next;
    while(ppptr!=ptr){
       ppptr=ppptr->next;
       pptr=pptr->next;
   }
   pptr->next=ppptr->next;
   free(ppptr);
   return head;
    
}
struct Node * deletionatlast(struct Node* head){
    struct Node *ptr = head;
    struct Node *pptr = head->next;
    while(pptr->next!=NULL){
        pptr=pptr->next;
        ptr=ptr->next;
    }
    ptr->next=NULL;
    free(pptr);  
    return head;
} 
struct Node * deletionfromfirst(struct Node* head){
    struct Node*ptr=head;
    head=head->next;
    free(ptr);
    return head;
    
}

int main(){
    struct Node* head;
    struct Node* second;
    struct Node* third;
    struct Node* fourth;
    struct Node* fifth;

    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    fourth=(struct Node*)malloc(sizeof(struct Node));
    fifth=(struct Node*)malloc(sizeof(struct Node));

    head->data=10;
    head->next=second;

    second->data=20;
    second->next=third;

    third->data=30;
    third->next=fourth;

    fourth->data=40;
    fourth->next=fifth;

    fifth->data=50;
    fifth->next=NULL;

Display(head);
printf("hello hello hello 1\n");
head=deletionfromfirst(head);
Display(head);
printf("hello hello hello 2\n");
head=deletionatlast(head);
Display(head);
printf("hello hello hello 3\n");
head=deletionatnode(head,second);
Display(head);
printf("hello hello hello 4\n");
head=deletioninbetween(head,4);
Display(head);
}