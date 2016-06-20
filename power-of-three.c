#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPowerOfThree(int n) {
    switch (n) {
    case 1:
    case 3:
    case 9:
    case 27:
    case 81:
    case 243:
    case 729:
    case 2187:
    case 6561:
    case 19683:
    case 59049:
    case 177147:
    case 531441:
    case 1594323:
    case 4782969:
    case 14348907:
    case 43046721:
    case 129140163:
    case 387420489:
    case 1162261467:
        return true;
    default:
        return false;
    }
}

void printBit(int n) {
    int i;

    for (i = 31; i >= 0; i--) {
        if (n & 0x1 << i) printf("1");
        else              printf("0");
        if (0 == i % 4) {
            printf(" ");
        }
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    int i;
    int count;
    
    printf("%d\n", isPowerOfThree(1));

    for (i = 3, count = 0; i > 0; i *= 3, count++) {
        printf("case %d:\n", i);
        /* printBit(i); */
    }
    printf("\n%d\n", count);

    /* printf("%s\n", ); */
    return 0;
}
