#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

/**
 * Other Solutions:
 * 
 *  1. f[i] = f[i / 2] + i % 2
 *  2. f[i] = f[i&(i-1)] + 1
 */


/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int scale;
    int *returnArray;
    int i;
    
    *returnSize = num + 1;
    returnArray = malloc(sizeof(int) * *returnSize);
    memset(returnArray, 0, sizeof(int) * *returnSize);
    returnArray[0] = 0;
    returnArray[1] = 1;
    for (i = 2, scale = 1; i < *returnSize; i++) {
        if (scale < i && scale << 1 <= i)
            scale <<= 1;
        returnArray[i] = 1 + returnArray[i ^ scale];
    }
    return returnArray;
}

int main(int argc, char *argv[])
{
    int *p;
    int returnSize;
    int i;

    p = countBits(1000, &returnSize);
    for (i = 0; i < returnSize; i++) {
        printf("%X:\t%d\n", i,  p[i]);
    }
    free(p);
    return 0;
}
