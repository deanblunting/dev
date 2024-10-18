#include <stdio.h>

int main() {
    int i;

    printf("Table of 5:\n");
    for (i = 1; i <= 10; i++) {
        printf("5 x %d = %d\n", i, 5 * i);
    }

    return 0;
}
