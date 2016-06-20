#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int integerBreak(int n) {
    int *optimum;
    int i, j;
    int currentBest;

    optimum = malloc(sizeof(int) * (n + 1));
    memset(optimum, 0, sizeof(int) * (n + 1));

    optimum[0] = optimum[1] = 0;
    optimum[2] = 1;
    for (i = 3; i < n+1; i++) {
        for (j = i - 1; j >= (i-1)/2; j--) {
            currentBest = max(j, optimum[j]) * max(i-j, optimum[i-j]);
            optimum[i] = max(optimum[i], currentBest);
        }
    }
    currentBest = optimum[n];
    free(optimum);
    return currentBest;
}

int main(int argc, char *argv[])
{
    printf("%d\n", integerBreak(2));
    printf("%d\n", integerBreak(10));
    return 0;
}
