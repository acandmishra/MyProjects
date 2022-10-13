#include<stdio.h>
#include<conio.h>
int swap(int arr[],int b){
    int i;
    int a=0;
    for(i=0;i<(b-1);i+=2){
        a = arr[(i)];
        arr[i]=arr[(i+1)];
        arr[(i+1)]=a;
    }
    for(i=0;i<b;i++){
        printf("%d\n",arr[i]);
    }
    return 0;
}
int main(){
    int i,a;
    printf("enter your array size: ");
    scanf("%d",&a);
    int arr[a];
    for(i=0;i<a;i++){
        printf("enter element %d: ",(i+1));
        scanf("%d",&arr[i]);
    }
    swap(arr,a);
    return 0;
}