#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int countNumbersWithUniqueDigits(int n) {
    int sum, num, choice;
    int i, j;

    sum = 1;                                    // n == 0 -> sum == 1, as for leetcode
    for (i = 1; i <= n && i <= 10; i++) {       // i <= 10: number over 10 digit duplicate.
        num = 9;                                // 1st digit should be [1-9]
        for (j = 2, choice = 9; j <= i; j++, choice--) {
            num *= choice;
        }
        sum += num;
    }
    return sum;
}

int countNumbersWithUniqueDigits_hack(int n) {
    int res[] = { 1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691 };
    if (n > 10) return res[10];
    else        return res[n];
}

int main(int argc, char *argv[])
{
    int i;
    for (i = 0; i < 12; i++) {
        printf("%d\n", countNumbersWithUniqueDigits(i));
    }
    return 0;
}
