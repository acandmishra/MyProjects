#include<stdio.h>
#include<stdlib.h>

struct Node{
    struct Node*left;
    int data;
    struct Node*right;
};

struct Node*Create(int data){
    struct Node*ptr = (struct Node*)malloc(sizeof(struct Node));
    ptr->left=NULL;
    ptr->data=data;
    ptr->right=NULL;
    return ptr;
}
struct Node*PreOrder(struct Node*root){
    if(root!=NULL){
        printf("%d ",root->data);
        PreOrder(root->left);
        PreOrder(root->right);
    }
    return 0;
}
struct Node*PostOrder(struct Node*root){
    if(root!=NULL){
        PostOrder(root->left);
        PostOrder(root->right);
        printf("%d ",root->data);
    }
    return 0;
}
struct Node*InOrder(struct Node*root){
    if(root!=NULL){
        InOrder(root->left);
        printf("%d ",root->data);
        InOrder(root->right);
    }
    return 0;
}
struct Node*SearchRecursive(struct Node*root,int key){
        if (root == NULL){
            return NULL;
        }
        if(root->data==key){
            (printf("\nelement found"));
            return 0;
            
        }
        else if(root->data>key){
            SearchRecursive(root->left,key);
            return 0;
        }
        else{
            SearchRecursive(root->right,key);
            return 0;
        }
    }
struct Node* SearchIterative(struct Node*root,int key){
    while(root!=NULL){
        if(root->data==key){
            (printf("\nelement found"));
            return 0;
            
        }
        else if(root->data>key){
            root = root->left;
            
        }
        else{
            root = root->right;
            
        }
    }
}

struct Node*Insert(struct Node*root,struct Node*ptr,int data){
    struct Node*p = root;
    struct Node*pp = NULL;
    ptr = Create(data);
    while(p!=NULL){
        if(p->data==data){
            printf("duplicate values!!");
            exit(0);
        }
        else if(data>p->data){
            pp = p;
            p = p->right;

        }
        else{
            pp = p;
            p = p->left;
        }
    }
    if(data>pp->data){
        pp->right = ptr;
    }
    else{
        pp->left = ptr;
    }
    

}

int main(){
   struct Node*root = Create(10);
   struct Node*chl = Create(3);
   struct Node*chr = Create(16);
   struct Node*gcll = Create(1);
   struct Node*gclr = Create(7);
   struct Node*gcrl = Create(14);

   root->left = chl;
   root->right = chr;

   chl->left = gcll;
   chl->right = gclr;

   chr->left = gcrl;


   PreOrder(root);
   printf("\n");
   PostOrder(root);
   printf("\n");
   InOrder(root);
   SearchRecursive(root,10);
   SearchIterative(root,10);
   printf("\n");
   PreOrder(root);
   printf("\n");
   struct Node*New1;
   Insert(root,New1,0);
   PreOrder(root);
   return 0;
}