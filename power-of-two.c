#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPowerOfTwo(int n) {
    return  n > 0 && (n & (n - 1)) == 0;
}

int main(int argc, char *argv[])
{
    printf("%d\n", isPowerOfTwo(19));
    printf("%d\n", isPowerOfTwo(6));
    printf("%d\n", isPowerOfTwo(8));
    printf("%d\n", isPowerOfTwo(16));
    printf("%d\n", isPowerOfTwo(-16));
    printf("%d\n", isPowerOfTwo(0));
    printf("%d\n", isPowerOfTwo(1));
    return 0;
}
