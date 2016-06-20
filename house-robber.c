#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int rob(int* nums, int numsSize) {
    int maxPre1, maxPre2, maxCur;
    int i;

    if (0 == numsSize) return 0;
    if (1 == numsSize) return nums[0];

    maxPre2 = nums[0];
    maxPre1 = max(nums[1], nums[0]);
    maxCur = max(maxPre2, maxPre1);
    for (i = 2; i < numsSize; i++) {
        maxCur = max(nums[i] + maxPre2, maxPre1);
        maxPre2 = maxPre1;
        maxPre1 = maxCur;
    }
    return maxCur;
}

int main(int argc, char *argv[])
{
    int a[] = {2, 1, 1, 2};
    printf("%d\n", rob(a, 4));
    return 0;
}
