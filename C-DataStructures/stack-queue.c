/* struct s {
  int top;
  int capacity;
  int *array;
};

typedef s stack;

stack* createStack(int capacity) {
  stack* new = (stack*) malloc(sizeof(stack));
  new -> capacity = capacity;
  new -> top = -1;
  new -> array = (int*)malloc(new -> capacity * sizeof(int));
  return new;
}

void push(stack* s, int item) {
  s -> array[++s->top] = item;
}

void pop(stack* s) {
  return s-> array[s->top--];
}
 */

/* ---------------------------------------------------------------------------- */

/* struct s {
  int data;
  stack* next;
};

typedef s stack;

stack* newNode(int data ) {
  stack* new = (stack*)malloc(sizeof(stack));
  new -> data = data;
  new -> next = null;
}

void push(stack* root, int data) {
  stack* temp = newNode(data);
  temp -> next = root;
  root = temp;
}

int pop(stack* root){
  stack* temp = root;
  root = root -> next;
  int popped = temp -> data;
  free(temp);
  return popped;
} */

/* -------------------------------------------------------------------------------------------------------- */

/* struct q {
  int head, tail, size;
  int capacity;
  int *array;
};

typedef q queue;

queue* createQueue(int capacity) {
  queue* new = (queue*)malloc(sizeof(queue));
  new->capacity = capacity;
  new -> head = new -> size = 0;
  new -> tail = capacity - 1;
  new -> array = (int*) malloc(new->capacity * sizeof(int));
}

void enqueue(queue* Queue, int item) {
  Queue -> tail = (Queue -> tail + 1) % Queue -> capacity;
  Queue -> array[Queue->tail] = item;
  Queue -> size = Queue -> size + 1;
}

int dequeue(queue* Queue) {
  int item = Queue->array[Queue->head];
  Queue->head = (Queue->head + 1) % Queue -> capacity;
  Queue -> size = Queue-> size - 1;
  return item;
} */

/* -------------------------------------------------------------------------------------------------------- */

struct Q {
  int data;
  QNode* next;
};

typedef Q QNode;

struct Que{
  QNode *head, *tail;
};

typedef Que Queue;

QNode* newNode(int k) {
  QNode* temp = (QNode*)malloc(sizeof(QNode));
  temp -> data = k;
  temp -> next = NULL;
  return temp;
}

Queue* createQueue() {
  Queue* q = (Queue*)malloc(sizeof(Queue));
  q->head = q->tail = NULL;
  return q;
}

void enQueue(Queue* q, int k) {
  QNode* temp = newNode(k);
  
  if(q->tail == NULL) {
    q->head = q->tail = temp;
    return;
  }
  q->tail->next = temp;
  q->rear = temp;
}

QNode* deQueue(Queue* q) {
  if(q->head == NULL) 
    return NULL;

    QNode* temp = q->head;
    q-> head = q->head->next;
}