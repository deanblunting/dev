#include <stdio.h>
int main() {
  int a, b, c;
  printf("Enter the value of A, B & C: \n");
  scanf("%d %d %d", &a, &b, &c);

  if (a >= b && a >= c)
    printf("%d is the largerst number", a);

  if (b >= a && b >= c)
    printf("%d is the largerst number", b);

  if (c >= b && c >= a)
    printf("%d is the largerst number", c);
}
