#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int diff;
    int i;
    int *returnArray = malloc(sizeof(int) * 2);

    *returnSize = 2;
    memset(returnArray, 0, sizeof(int) * 2);

    for (i = 0, diff = 0; i < numsSize; i++)
        diff ^= nums[i];
    diff = diff & diff - 1 ^ diff;
    for (i = 0; i < numsSize; i++)
        if ((diff & nums[i]) == 0) returnArray[0] ^= nums[i];
        else                       returnArray[1] ^= nums[i];

    return returnArray;
}

int main(int argc, char *argv[])
{
    int *resultArray;
    int returnSize;
    int array[] = {1, 2, 3, 4, 2, 1, 8, 8, 9, 9, 0, 0};
    int len = 12;
    int i;

    resultArray = singleNumber(array, len, &returnSize);
    for (i = 0; i < returnSize; i++) {
        printf("%d\n", resultArray[i]);
    }
    return 0;
}
