#include <stdio.h>
int main() {
  int num1, num = 8;
  printf("Enter the value of num 1: ");
  scanf("%d", &num1);

  if (num1 > num) {
    printf("%d is greater", num1);
  } else {
    printf("%d is smaller", num1);
  }
  return 0;
}
