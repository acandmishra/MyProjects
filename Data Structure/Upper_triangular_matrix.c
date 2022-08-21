#include<stdio.h>
#include<stdlib.h>

int triangle (int arr[][3])
{
    int pro = 1;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
          if(i==j){
            pro *= arr[i][j];
          }

        }
        
    }
    return pro;
}
int main(){
    int UT;
    int arr[3][3];
    printf("enter the elements of 3x3 matrix\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("enter element at index (%d,%d):",i,j);
            scanf("%d",&arr[i][j]);
        }
        
    }
    UT=triangle(arr);
    printf("%d",UT);
    return 0;
}