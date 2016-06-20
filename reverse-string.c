#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

char* reverseString(char* s) {
    int lo, hi;

    for (hi = 0; s[hi]; ++hi) {
    }
    for (lo = 0, --hi; lo < hi; ++lo, --hi) {
        s[lo] ^= s[hi];
        s[hi] ^= s[lo];
        s[lo] ^= s[hi];
    }
    return s;
}

int main(int argc, char *argv[])
{
    char s[100] = "C mode defined in `cc-mode.el`";
    int a = 1, b = 100;
    a ^= b;
    b ^= a;
    a ^= b;
    printf("%d, %d\n", a, b);
    printf("%s\n", reverseString(s));
    return 0;
}
