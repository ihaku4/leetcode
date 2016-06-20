#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

// https://leetcode.com/discuss/67755/3-methods-for-python-with-explains
int addDigits(int num) {
    int sum = num % 9;

    if (0 == num) return 0;
    return (0 == sum) ? 9 : sum;
}

int addDigits2(int num) {
    int sum;

    while (num / 10) {
        sum = 0;
        while (num) {
            sum += num % 10;
            num /= 10;
        }
        num = sum;
    }
    return num;
}

int main(int argc, char *argv[])
{
    printf("%d\n", addDigits(38));
    return 0;
}
