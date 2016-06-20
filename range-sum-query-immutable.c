#include <stdio.h>
#include <stdlib.h>

struct NumArray {
    int num;
    int sum;
};

/** Initialize your data structure here. */
struct NumArray* NumArrayCreate(int* nums, int numsSize) {
    int i;

    if (numsSize <= 0) {
        return NULL;
    }

    struct NumArray *p = malloc(sizeof(struct NumArray) * numsSize);
    
    p[0].num = nums[0];
    p[0].sum = nums[0];
    for (i = 1; i < numsSize; i++) {
        p[i].num = nums[i];
        p[i].sum = nums[i] + p[i-1].sum;
    }
    return p;
}

int sumRange(struct NumArray* numArray, int i, int j) {
    if (0 == i) return numArray[j].sum;
    else        return numArray[j].sum - numArray[i-1].sum;
}

/** Deallocates memory previously allocated for the data structure. */
void NumArrayFree(struct NumArray* numArray) {
    free(numArray);
}

// Your NumArray object will be instantiated and called as such:
// struct NumArray* numArray = NumArrayCreate(nums, numsSize);
// sumRange(numArray, 0, 1);
// sumRange(numArray, 1, 2);
// NumArrayFree(numArray);

int main(int argc, char *argv[])
{
    
    return 0;
}
