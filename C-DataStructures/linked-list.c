#include <stdio.h>
#include <stdlib.h>

struct n {
  int x;
  node *next;
};

typedef n node;

int main() {
  node *root;
  root = ( node *)malloc(sizeof(node));
   node *iter;
  iter = root;
  while (iter != NULL) {
    iter = iter -> next;
    printf("%d", 6);
  }
}

void bastir(struct node *root) {
  while(r != NULL) {
    printf("%d", root->x);
    r = r->next;
  }
}

void ekle(node *root, int x) {
  while(r-> next != NULL) {
    r -> next = (node *)malloc(sizeof(node));
    r->next->x = x;
    r->next->next = NULL;
  }
} 

struct node * ekleSirali(struct node *r, int x) {
  if (r == NULL) {
    r = (node *)malloc(sizeof(node));
    r -> next = NULL;
    r -> x = x;
  }
  while (r-> next != NULL && r-> next ->x < x ){
    r = r-> next;
  }
  else if (r->next == NULL) {
    if(r->x > x) {
      struct node * temp = (node *)malloc(sizeof(node));
      temp -> x = x;
      temp -> next = root;
      r = temp;
      return temp;
    } else{
      struct node * temp = (node *)malloc(sizeof(node));
      temp -> x = x;
      temp -> next = NULL;
      r-> next = temp;
      return r;
    }
  }
}

node * sil(node *r, int x) {
  node *temp;
  node *iter = r;
  if (r-> x == x) {
    temp = r;
    r = r->next;
    free(temp);
    return r;
  }
  while (iter->next != NULL && iter->next->x != x) {
    iter = iter -> next;
  }
  if (iter -> next == NULL) {
    printf("sayi bulunamadi");
    return r;
  }
  temp = iter->next;
  iter->next = iter->next->next;
  free(temp);
  return r;
}

// Dairesel linked list
void bastir (node *r ) {
  node *iter = r;
  print
  while(iter != r) {
    printf("%d", )
  }
}

void ekle(node *r, int x) {
  node * iter = r;
  while(iter -> next != r) {
    iter = iter -> next;
  } 
  iter-> next = (node*)malloc(sizeof(node));
  iter->next->x = x;
  iter->next->next = r;
}

node * ekleSirali(node *r, int x) {
  if (r = NULL) {
    r = (node *)malloc(sizeof(node));
    r->next = r;
    r->x = x;
    return r;
  }
  if(r->x > x){
    node * temp = (node *)malloc(sizeof(node));
    temp -> x = x;
    temp -> next = r;
    node *iter = r;
    while(iter->next!=r)
      iter = iter -> next;
    iter -> next = temp;
    return temp;
  }

}

struct n { 
  int x;
  n *prev;
  n *next;
}

typedef n node;

node * siraliEkle(node *r, int x) {
  if(r == NULL) {
    r = (node *)malloc(sizeof(node));
    r->next = NULL;
    r->prev = NULL;
    r->x = x;
    return r;
  }
}