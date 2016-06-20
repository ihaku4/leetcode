#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

void moveZeroes(int* nums, int numsSize) {
    int i, count;

    for (i = 0, count = 0; i < numsSize; i++) {
        if (0 == nums[i])
            ++count;
        else if (count)
            nums[i - count] = nums[i];
    }
    for (i = numsSize - count; i < numsSize; i++)
        nums[i] = 0;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
