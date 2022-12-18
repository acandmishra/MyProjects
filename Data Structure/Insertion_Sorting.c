#include<stdio.h>
#include<stdlib.h>

int Display(int arr[],int size){
    int i;
    for(i=0;i<size;i++){
        printf("element at index:%d->%d\n",i,arr[i]);
    }
}
int Insertion(int arr[],int size){
    int i,j;
    for(i=0;i<size-1;i++){
        printf("pass:%d\n",i+1);
        for(j=i+1;j>0;j--){
            printf("comparison:%d\n",j);
            if(arr[j-1]>arr[j]){
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
            Display(arr,size);
        }
    }
}

int main(){
    int arr[] = {27,3,2,1,9,4};
    int x = 6;
    Display(arr,x);
    Insertion(arr,x);
    printf("\n");
    Display(arr,x);

}