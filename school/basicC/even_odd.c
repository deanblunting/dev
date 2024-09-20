#include <stdio.h>
int main(void) {
  int x;
  printf("Enter a no: ");
  scanf("%d", &x);
  printf("%d", (x % 2) == 0);
  return 0;
}
