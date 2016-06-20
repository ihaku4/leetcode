#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPowerOfFour(int num) {
    if (0x1 << 0 == num ||
        0x1 << 2 == num ||
        0x1 << 4 == num ||
        0x1 << 6 == num ||
        0x1 << 8 == num ||
        0x1 << 10 == num ||
        0x1 << 12 == num ||
        0x1 << 14 == num ||
        0x1 << 16 == num ||
        0x1 << 18 == num ||
        0x1 << 20 == num ||
        0x1 << 22 == num ||
        0x1 << 24 == num ||
        0x1 << 26 == num ||
        0x1 << 28 == num ||
        0x1 << 30 == num) {
        return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    int i;

    for (i = 0; i < 32; i+=2) {
        printf("0x1 << %d == num ||\n", i);
    }
    printf("%d\n", isPowerOfFour(4));
    printf("%d\n", isPowerOfFour(5));
    printf("%d\n", isPowerOfFour(6));
    printf("%d\n", isPowerOfFour(7));
    printf("%d\n", isPowerOfFour(8));
    printf("%d\n", isPowerOfFour(9));
    printf("%d\n", isPowerOfFour(-8));
    printf("%d\n", isPowerOfFour(-9));
    printf("%d\n", isPowerOfFour(-4));
    printf("%d\n", isPowerOfFour(-5));
    printf("%d\n", isPowerOfFour(0x80000000));

    printf("\n");
    printf("%d\n", true);
    printf("%d\n", false);
    printf("%d\n", (4 & 0x3) == 0);
    printf("%d\n", 0x80000000);
    printf("%d\n", ~0x80000000 + 1);

    printf("0x%x\n", 8);
    printf("0x%x\n", -8);
    printf("0x%x\n", 4);
    printf("0x%x\n", -4);

    return 0;
}
