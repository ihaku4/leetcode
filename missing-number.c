#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int missingNumber(int* nums, int numsSize) {
    int i;
    int num = 0;

    for (i = 0; i < numsSize + 1; i++)
        num ^= i;
    for (i = 0; i < numsSize; i++)
        num ^= nums[i];
    return num;
}

int main(int argc, char *argv[])
{
    int arr[] = {0, 1, 3};
    printf("%d\n", missingNumber(arr, 3));
    return 0;
}
