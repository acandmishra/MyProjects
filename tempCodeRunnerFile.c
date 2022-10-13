#include<stdio.h>
int Display(int arr[],int size){
    for(int i=0;i<size;i++){
        printf("element at index:%d->%d\n",i,arr[i]);
    }
}


int Count(int arr[],int size){
   int i,j,k;
   int max;
   max=arr[0];
   for(i=0;i<size;i++){
    if(max<arr[i]){
        max=arr[i];
    }
    else{
        max=max;
    }
   }
   printf("max:%d\n",max);
   int Aux1[max+1];
   for(j=0;j<max+1;j++){
    Aux1[j] = 0;
   }
   for(i=0;i<size;i++){
    Aux1[arr[i]] = 1;
   }
   int Aux2[size];
   k=0;
   for(j=0;j<max+1;j++){
    while(Aux1[j]!=0){
        Aux2[k]=j;
        k++;
        Aux1[j]-=1;
    }
   } 
   Display(Aux2,size);
      
}

int main(){
    int arr[]={72,48,12,61,84,36,9};
    int size = 7;
    Display(arr,size);
    Count(arr,size);
}