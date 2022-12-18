#include <stdio.h>
#include <stdlib.h>
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

void Count(struct Node*ptr,int data){
    int count = 0;
    while(ptr!=NULL){
        if(ptr->data==data){
            count+=1;
        }
    ptr=ptr->next;
    }
    printf("count of %d is:%d",data,count);
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

    head->data=1;
    head->next=second;

    second->data=7;
    second->next=third;

    third->data=2;
    third->next=fourth;

    fourth->data=7;
    fourth->next=NULL;

Display(head);
Count(head,7);

}