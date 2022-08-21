#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};

void Display(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element:%d\n", ptr->data);
        ptr = ptr->next;
    }
}
struct Node *InsertAtFirst(struct Node *head, int value)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = value;
    ptr->next = head;
    return ptr;
}
struct Node *InsertInBetween(struct Node *head, int value, int index)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = value;
    struct Node *p = head;
    int i = 0;
    while (i != index - 1)
    {
        p = p->next;
        i++;
    }
    ptr->next = p->next;
    p->next = ptr;
}
struct Node *InsertAtEnd(struct Node *head, int number)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = number;
    struct Node *p = head;
    while (p->next != NULL)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->next = NULL;
    return head;
}
struct Node* InsertAfterNode(struct Node*head,struct Node* prevnode,int value){
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->data=value;
    ptr->next=prevnode->next;
    prevnode->next=ptr;
    return head;
}
int main()
{
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    head->data = 10;
    head->next = second;

    second->data = 20;
    second->next = third;

    third->data = 30;
    third->next = fourth;

    fourth->data = 40;
    fourth->next = NULL;
    long int x = 111111;
    Display(head);
    printf("%ld\n", x);
    head = InsertAtFirst(head, 32);
    Display(head);
    printf("%ld\n", x);
    printf("enter the index at which you want to add the node:");
    int a, d = 0;
    scanf("%d", &a);
    printf("enter the data:");
    scanf("%d", &d);
    InsertInBetween(head, d, a);
    Display(head);
    printf("%ld\n", x);
    InsertAtEnd(head, 100);
    Display(head);
    printf("%ld\n", x);
    head=InsertAfterNode(head,second,100);
    Display(head);
}