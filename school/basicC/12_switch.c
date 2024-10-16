#include <stdio.h>

int main() {
  char grade = 'B';

  switch (grade) {
  case 'A':
    printf("excellent!\n");
    break;
  case 'B':
    printf("outstanding!\n");
    break;
  case 'C':
    printf("well done\n");
    break;
  case 'D':
    printf("you passed\n");
    break;
  case 'E':
    printf("better try again\n");
    break;
  default:
    printf("invalid grade\n");
    break;
  }

  printf("your grade is %c\n", grade);
  return 0;
}
