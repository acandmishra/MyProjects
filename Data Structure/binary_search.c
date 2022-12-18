#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int binary_search(int arr[],int size,int element){
    int low=0;
    int high=(size-1);
    while(low<=high){
        int mid = (low+high)/2;
        if(arr[mid]==element){
            printf("the element is found at index:%d",mid);
            exit (0);
        }
        else if(arr[mid]<element){
            low=(mid+1);
        }
        else{
            high=(mid-1);
        }
    }
    return -1;
}
int main(){
    int element,output,arr[]={1,2,3,4,5,6,7,8,9,10,11,12}; // sorted array is a must
    int length = (sizeof(arr)/sizeof(int));
    printf("the array size is:%d\n",length);
    printf("enter the element you wanna search for:");
    scanf("%d",&element);
    output =binary_search(arr,length,element);
    if(output==-1){
        printf("not found");
    }
    return 0;


}