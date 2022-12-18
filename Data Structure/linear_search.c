#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int main(){
int arr[10]={1,2,3,4,5,6,7,8,9,10};
int i,a,f;
printf("enter the element you want to search");
scanf("%d",&a);
for(i=0;i<10;i++){
    if(arr[i]==a){
        printf("element found at index:%d",i);
        exit(0);
    }
    else{
        f=1;
    }
}
if(f==1){
    printf("Not found");
}
return 0;
}