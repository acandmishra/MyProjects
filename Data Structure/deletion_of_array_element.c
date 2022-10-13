#include <stdio.h>
int main(){
    int i,a;
    int arr[]={1,2,3,4,5,6,7,8,9,10};
    int size = (sizeof(arr)/sizeof(int));
    printf("enter the index for deletion:");
    scanf("%d",&a);
    for(i=(a+1);i<size;i++){
        arr[i-1]= arr[i];
    }
    size-=1;
    printf("the new array is:");
    for(i=0;i<size;i++){
        printf("%d,",arr[i]);
    }
    return 0;
}