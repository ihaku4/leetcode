#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

bool canWinNim(int n) {
    /* return n % 4 != 0; */
    return (n & 0x3) != 0;
}

bool canWinNim2(int n) {
    bool W[3] = {true, true, true};
    bool canwin;
    int count;

    if (n <= 3) return W[n - 1];

    for (count = 4; count <= n; ++count) {
        canwin = !(W[0] && W[1] && W[2]);
        W[0] = W[1];
        W[1] = W[2];
        W[2] = canwin;
    }
    return canwin;
}

int main(int argc, char *argv[])
{
    int i;

    for (i = 1; i < 100; i++) {
        printf("%d\n", canWinNim(i) == canWinNim2(i));
        /* printf("%d\n", canWinNim2(i)); */
    }
    return 0;
}
