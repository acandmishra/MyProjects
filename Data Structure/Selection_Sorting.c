#include<stdio.h>
#include<stdlib.h>

int Display(int arr[],int size){
    for(int i=0;i<size;i++){
        printf("element at index:%d->%d\n",i,arr[i]);
    }
}


void Selection(int arr[],int size){
    for(int i=0;i<size-1;i++){
        int min_index=i;
        printf("pass:%d\n",i+1);
        for(int j=i+1;j<size;j++){
            printf("comparison:%d\n");
            if(arr[j]<arr[min_index]){
                min_index = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
        
        Display(arr,size);
    }
}
int main(){
    int arr[] = {27,9,72,81,6,12,0};
    int size = 7;
    Display(arr,size);
    Selection(arr,size);
    printf("\n");
}