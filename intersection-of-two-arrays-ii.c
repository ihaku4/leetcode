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
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int * returnNums;
    int i, j;

    returnNums = malloc(sizeof(int) * max(nums1Size, nums2Size));
    *returnSize = 0;

    qsort(nums1, nums1Size, sizeof(int), compare_ints);
    qsort(nums2, nums2Size, sizeof(int), compare_ints);

    for (i = 0, j = 0; i < nums1Size && j < nums2Size; i++) {
        for (;j < nums2Size; j++) {
            if (nums1[i] < nums2[j]) {
                break;
            }
            if (nums1[i] == nums2[j]) {
                returnNums[*returnSize] = nums1[i];
                ++*returnSize;

                j++;
                break;
            }
        }
    }

    return returnNums;
}

int main(int argc, char *argv[])
{
    /* int a[] = {1, 2, 3, 4, 5, 6}; */
    /* int b[] = {5, 3, 6}; */
    /* int lena = 6, lenb = 3; */
    /* int a[] = {1, 2, 2, 1}; */
    /* int b[] = {2}; */
    /* int lena = 4, lenb = 1; */

    int a[] = {9,1};
    int b[] = {7,8,3,9,0,0,9,1,5};
    int lena = 2, lenb = 9;
    int *c;
    int len;
    int i;
    
    printf("%d\n", INT_MIN);
    printf("%d\n", -INT_MIN);
    printf("%d\n", INT_MIN - 1);

    /* qsort(a, lena, sizeof(int), compare_ints); */
    /* for (i = 0; i < lena; i++) { */
    /*     printf("%d ", a[i]); */
    /* } */
    /* printf("\n"); */

    c = intersect(a, lena, b, lenb, &len);
    for (i = 0; i < len; i++) {
        printf("%d ", c[i]);
    }
    printf("\n%d\n", len);
    free(c);
    return 0;
}
