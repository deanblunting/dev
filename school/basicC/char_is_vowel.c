#include <stdio.h>
int main() {
  char character;
  printf("Enter a character: ");
  scanf("%c", &character);

  if (character == 'a') {
    printf("its a vowel\n");
  }

  else if (character == 'e') {
    printf("its a vowel\n");
  }

  else if (character == 'i') {
    printf("its a vowel\n");
  } else if (character == 'o') {
    printf("its a vowel\n");
  } else if (character == 'u') {
    printf("its a vowel\n");
  } else {
    printf("its not a vowel\n");
  }
  return 0;
}
