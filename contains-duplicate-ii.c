#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    int i, j;

    for (i = 0; i < numsSize; i++)
        for (j = i + 1; j < numsSize && j - i <= k; j++)
            if (nums[i] == nums[j])
                return true;
    return false;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
