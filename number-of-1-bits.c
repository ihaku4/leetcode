#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

    
int hammingWeight(uint32_t n) {
    int i, count = 0;

    for (i = 31; i >= 0; i--)
        if (n & 0x1 << i) count++;
    return count;
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
    
    for (i = 3, count = 0; i > 0; i *= 3, count++) {
        printf("case %d:\n", i);
        /* printBit(i); */
    }
    printf("\n%d\n", count);

    /* printf("%s\n", ); */
    printf("%d\n", hammingWeight(11));
    printf("%d\n", hammingWeight(0));
    return 0;
}
