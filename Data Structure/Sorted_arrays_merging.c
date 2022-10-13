#include <stdio.h>
int Display(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("element at index:%d->%d\n", i, arr[i]);
    }
}

int Merge(int a[], int b[], int c[], int m, int n)
{
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < m && j < n)
    {
        if (a[i] < b[j])
        {
            c[k] = a[i];
            i++, k++;
        }
        else
        {
            c[k] = b[j];
            j++, k++;
        }
    }
    while (i < m)
    {
        c[k] = a[i];
        i++, k++;
    }
    while (j < n)
    {
        c[k] = b[j];
        j++, k++;
    }
    Display(c, (m + n));
}

int main()
{
    int A[] = {12, 27, 34, 46, 58};
    int B[] = {1, 2, 54, 67};
    int s1 = 5;
    int s2 = 4;
    int C[s1 + s2];
    Display(A, s1);
    printf("\n");
    Display(B, s2);
    printf("\n");
    Merge(A, B, C, s1, s2);
}