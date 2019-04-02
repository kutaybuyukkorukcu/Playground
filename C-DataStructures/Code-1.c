#include <stdio.h>
#include <stdlib.h>

int main() {
  int *p, secim = 1, i;
  char secim;
  p = (int *)malloc(sizeof(int) * 2);
  if (p = NULL) {
    printf("Yer ayrilamadi");
  }
  while(secim != 0) {
    printf("Sehir giriniz:");
    scanf("%s", &secim);
    p[sayac] = secim;
    sayac++;
    p = (int *)realloc(p, sizeof(int) * (sayac + 1));
  } 
  for(i = 0;i<sayac;i++){
    printf("%s\t",p[i]);
  }
  free(p);
  return 0;
}