#include<stdio.h>
int main(){
    int a=10;
    int*ptr=&a;
    printf("%u\n",ptr);
    printf("%u\n",&a);
    printf("%d\n",*ptr);
    return 0;
}