struct p{
  int data;
  person *next;
};

typedef p person;
person* top = NULL;
person* temp;

person* createPerson(int data) {
  person* newPerson = (person *)malloc(sizeof(person));
  newPerson -> data = data;
  return newPerson;
}

void pushNode(int data) {
  person* newFirst = createPerson(data);
  newFirst -> next = top;
  top = newFirst;
}

void popNode() {
  temp = top -> next;
  free(top);
  top = temp;
}

