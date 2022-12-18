#include<stdio.h>
#include<stdlib.h>

void insert(int arr[],int element,int size,int u_size,int index){
    if(index>=size){
        printf("oops!cannot insert");
        exit(0);
    }
    for(int i=u_size;i>=index;i--){
        arr[i+1]=arr[i];
    }
    arr[index]=element;
    
}


int main(){
    int arr[100]={0,1,2,3,4,5,6,7,8,9};
    int size=sizeof(arr)/sizeof(int);
    printf("%d\n",size);
    int u_size=10;
    for(int i=0 ; i<u_size ;i++){
        printf("%d ",arr[i]);
    }
    
    printf("\nenter the element to be inserted\n");
    int a,b;
    scanf("%d",&a);
    printf("enter the index on which the element is to be inserted");
    scanf("%d",&b);
    insert(arr,a,size,u_size,b);
    u_size+=1;
    for(int i=0 ; i<u_size ;i++){
        printf("%d ",arr[i]);
    }
    return 0;

}