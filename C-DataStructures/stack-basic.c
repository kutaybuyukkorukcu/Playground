/* int *dizi;
int boyut = 2;
int tepe = 0;

int pop() {
  if (tepe <= boyut / 4) {
    int *dizi2 = (int *)malloc(sizeof(int) * boyut / 2);
    for(int i = 0;i<boyut; i++) {
      dizi2[i] = dizi[i];
    }
    free(dizi);
    dizi = dizi2;
    boyut /= 2;
  }
  return dizi[--tepe];
}

void push(int a){
  if(tepe >= boyut) {
    int *dizi2 = (int*)malloc(sizeof(int) * boyut * 2);
    for(int i =0;i<boyut;i++) {
      dizi2[i] = dizi[i];
    }
    free(dizi);
    dizi = dizi2;
    boyut *= 2;
  }
  dizi[tepe++] = a;
} */

/* --------------------------------------------------- */ 

struct s {
  int boyut;
  int tepe;
  int *dizi;
}

typedef s stack;

stack* tanim() {
  stack *sa = (stack *)malloc(sizeof(stack));
  sa->boyut = 2;
  sa->tepe = 0;
  sa->dizi = NULL;
  return sa;
}

void push(int a, stack *s) {
  if(s-> dizi == NULL) {
    s-> dizi = (int*)malloc(sizeof(int) * 2);
  }
  if(s->tepe >= s->boyut - 1){
    int *dizi2 = (int*)malloc(sizeof(int) * s->boyut*2);
    for(int i = 0;i<s->boyut ; i++) {
      dizi2[i] = s-> dizi[i];
    }
    free(s->dizi);
    s->dizi = dizi2;
    s->boyut *= 2;
  }
  s->dizi[tepe++] = a;
}

int pop(stack *s) {
  if(s->dizi == NULL || s-> tepe <= 0) {
    printf("dizi bos");
    return -1;
  }
  if(s->tepe <= s->boyut/4){
    int *dizi2 = (int*)malloc(sizeof(int) * s-> boyut / 2);
    for(int i = 0;s->tepe;i++) {
      dizi2[i] = s-> dizi[i];
    }
    free(s->dizi);
    s-> dizi = dizi2;
    s-> boyut /= 2;
  }
  return s->dizi[s->--tepe];
}