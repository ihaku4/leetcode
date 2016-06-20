#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int compare_ints(const void *a, const void *b) {
    int arg1 = *(const int *) a;
    int arg2 = *(const int *) b;
    return (arg1 > arg2) - (arg1 < arg2);
}

bool containsDuplicate(int* nums, int numsSize) {
    int i;

    qsort(nums, numsSize, sizeof(int), compare_ints);
    for (i = 0; i < numsSize-1; i++)
        if (nums[i] == nums[i+1])
            return true;
    return false;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
