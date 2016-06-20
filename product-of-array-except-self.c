#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *returnArray;
    int i;
    int accum;

    *returnSize = numsSize;
    returnArray = malloc(sizeof(int) * numsSize);

    accum = 1;
    for (i = 0; i < numsSize; i++) {
        returnArray[i] = accum;
        accum *= nums[i];
    }
    accum = 1;
    for (i = numsSize - 1; i >= 0; i--) {
        returnArray[i] *= accum;
        accum *= nums[i];
    }
    return returnArray;
}

int main(int argc, char *argv[])
{
    int nums[] = {1, 2, 3, 4, 5};
    int len = 5;
    int returnSize;
    int *returnArray, *tofree;
    int i;

    tofree = returnArray = productExceptSelf(nums, len, &returnSize);
    for (i = 0; i < len; i++) {
        printf("%d\n", returnArray[i]);
    }
    free(tofree);
    return 0;
}
