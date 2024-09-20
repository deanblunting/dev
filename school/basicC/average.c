#include <stdio.h>
int main() {
  int a, b, c;
  printf("Use comma to separate each number\n");
  printf("Enter numbers: ");
  scanf("%d, %d, %d", &a, &b, &c);
  printf("Average is: %d", (a + b + c) / 3);
  return 0;
}
