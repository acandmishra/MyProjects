#include <stdio.h>
#include <stdlib.h>

struct MyArr{
        int total_size;
        int used_size;
        int *ptr;

    };

void create_array(struct MyArr *a , int t_size , int u_size){
    (*a).total_size = t_size; // (*a) is used to dereference the pointer
    (*a).used_size = u_size;
    (*a).ptr = (int*)malloc(t_size*sizeof(int));

}
void insert(struct MyArr *a){
    printf("insert values\n");
    for ( int i = 0; i < (*a).used_size; i++)
    {
        scanf("%d", &(*a).ptr[i]);

    }
}
void show(struct MyArr *a){
    for ( int i = 0; i < (*a).used_size; i++)
    {
        printf("%d", (*a).ptr[i]);
    }
    
}

int main(){
    struct MyArr marks;
    create_array(&marks,100,5);
    insert(&marks);
    show(&marks);
    return 0;

}

    