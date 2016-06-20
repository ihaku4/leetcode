#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int divide_slow(int dividend, int divisor) {
    int negative = dividend < 0 ^ divisor < 0;
    int res = 0;

    if (0 == divisor) return INT_MAX;
    if (0 == dividend)  return 0;

    // both negative for INT_MIN
    if (dividend > 0) dividend = -dividend;
    if (divisor > 0) divisor = -divisor;

    while (dividend <= divisor) {
        dividend -= divisor;            //XXX: This is Slow!
        res++;
    }
    return negative ? -res : res;
}

int divide(int dividend, int divisor) {
    int negative = dividend < 0 ^ divisor < 0;
    int res = 0, restmp;
    int num, sum;

    if (0 == divisor) return INT_MAX;
    if (0 == dividend)  return 0;

    // both negative for INT_MIN
    if (dividend > 0) dividend = -dividend;
    if (divisor > 0) divisor = -divisor;

    if (dividend > divisor)
        return 0;

    sum = num = 0;
    res = 0;
    while (dividend <= sum + divisor + divisor && sum + divisor + divisor < 0) {
        num = divisor;
        restmp = 1;
        while (dividend <= sum + num + num && sum + num + num < 0) {
            restmp += restmp;
            num += num;
        }
        if (1 != restmp) {
            sum += num;
            res += restmp; 
        }
    }

    while (dividend <= sum + divisor && sum + divisor < 0) {
            res += 1;
            sum += divisor;
    }
    if (!negative && res == INT_MIN)
        return INT_MAX;
    return negative ? -res : res;
}

int main(int argc, char *argv[])
{
    printf("%d\n", divide(15, 3));
    printf("%d\n", divide(100, 3));
    printf("%d\n", divide(1000, 250));
    printf("%d\n", divide(1024, 2));

    printf("%d\n", divide(-15, 3));
    printf("%d\n", divide(-100, 3));
    printf("%d\n", divide(-1000, 250));
    printf("%d\n", divide(-1024, 2));

    printf("%d\n", divide(2147483647, 1));
    return 0;
}
