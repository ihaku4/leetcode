#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int compare_ints(const void *a, const void *b) {
    int arg1 = *(const int *) a;
    int arg2 = *(const int *) b;
    return (arg1 > arg2) - (arg1 < arg2);
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int i, j;
    int *returnNums;

    returnNums = malloc(sizeof(int) * max(nums1Size, nums2Size));
    qsort(nums1, nums1Size, sizeof(int), compare_ints);
    qsort(nums2, nums2Size, sizeof(int), compare_ints);
    
    *returnSize = 0;
    for (i = 0, j = 0; i < nums1Size && j < nums2Size; i++) {
        for (; j < nums2Size; j++) {
            if (nums2[j] == nums1[i] &&
                !(*returnSize && returnNums[*returnSize - 1] == nums2[j]))
            {
                returnNums[*returnSize] = nums2[j];
                ++*returnSize;
                ++j;
                break;
            }
            if (nums2[j] > nums1[i])
                break;
        }
    }
    return returnNums;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
