#include <stdio.h>
#include <stdlib.h>

struct n {
  node *next;
  int data;
};

typedef n node;
int pop(node *);
void push(node *, int);

node* push (node *root, int a) {
  if(root == NULL) {
    root = (node *)malloc(sizeof(node));
    root -> data = a;
    root -> next = NULL;
    return root;
  }
  node* iter = root;
  while(iter->next != NULL) {
    iter = iter->next;
  }
  node* temp = (node*)malloc(sizeof(node));
  temp -> data = a;
  temp -> next = NULL;
  iter -> next = temp;
  return root;
} 

int pop (node *root) {
  if (root == NULL) {
    printf("Stack bos");
    return -1;
  }
  node *iter = node;
  while(iter->next->next != NULL) {
    iter = iter->next;
  } 
  if(root -> next == NULL) {
    int rvalue = root -> data;
    free(root);
    return rvalue;
  }
  node *temp = iter->next;
  int rvalue = temp->data;
  iter->next = iter->next->next;
  free(temp);
  return rvalue;
} 
