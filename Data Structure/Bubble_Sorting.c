#include<stdio.h>
#include<stdlib.h>

void Display(int arr[],int size){
    for(int i=0;i<size;i++){
        printf("%d ",arr[i]);
    } 
    printf("\n");
}

void Bubble(int arr[],int size){
    int i,j;
    for(i=0;i<size-1;i++){
        printf("\npass:%d",i+1);
        for(j=0;j<size-i-1;j++){
            printf("\ncomparison:%d\n",j+1);
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                Display(arr,size);
            }
        }
    }
}

int main(){
    int s,i;
    printf("size of array:");
    scanf("%d",&s);
    int arr[s];
    for(i=0;i<s;i++){
        printf("enter the element:");
        scanf("%d",&arr[i]);
    }   
    Display(arr,s); 
    printf("\nSORTING ARRAY\n");
    Bubble(arr,s);
    printf("the final sorted array is:\n");
    Display(arr,s);
    
}