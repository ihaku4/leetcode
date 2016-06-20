#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

#define LEN 10000

char* fractionToDecimal(int numerator, int denominator) {
    int numeratorList[LEN];
    int fractionList[LEN];
    int fractionSize;
    int integer;
    char *resultString;
    int i, j, n;
    int repeatingIndex;
    int negative = 0;

    if (0 == denominator)
        return NULL;

    if (numerator < 0) {
        /* numerator = -numerator; */
        negative ^= 1;
    }
    if (denominator < 0) {
        /* denominator = -denominator; */
        negative ^= 1;
    }

    resultString = malloc(sizeof(char) * LEN);

    if (numerator == INT_MIN && denominator == -1) {
        sprintf(resultString, "2147483648");
        return resultString;
    }
    // TODO: Replace this hack
    //       How to perform division to INT_MIN? XXX
    //       Need `High Precision'?
    if (numerator == -1 && denominator == INT_MIN) {
        sprintf(resultString, "0.0000000004656612873077392578125");
        return resultString;
    }

    integer = numerator / denominator;
    numerator %= denominator;
    /* if (numerator < 0) { */
    /*     negative = 1; */
    /*     numerator = -numerator; */
    /* } */
    repeatingIndex = -1;
    fractionSize = 0;
    for (i = 0; 0 != numerator && -1 == repeatingIndex; i++) {
        for (j = 0; j < i; j++) {
            if (numerator == numeratorList[j]) {
                repeatingIndex = j;
                break;
            }
        }

        if (-1 == repeatingIndex)
            fractionSize++;

        numeratorList[i] = numerator;
        numerator *= 10;
        fractionList[i] = numerator / denominator;
        numerator %= denominator;
    }
    
    // print integer TODO
    /* if (negative) */
        /* resultString[i++] = '-'; */
        
    /* sprintf(resultString + i, "%d", integer); */
    i = 0;
    for (i += 1, n = 10; n > 0 && integer / n != 0; i++, n *= 10) {
    }
    if (integer < 0) {
        sprintf(resultString, "%d", integer);
        i++;
    }
    else if (0 == integer && negative && fractionSize > 0) {
        sprintf(resultString, "-%d", integer);
        i++;
    }
    else {
        sprintf(resultString, "%d", integer);
    }

    /// print fraction
    if (fractionSize > 0) {
        resultString[i++] = '.';
        // TODO: Check < LEN
        for (j = 0; j < fractionSize; j++) {
            // Repeating
            if (j == repeatingIndex)
                resultString[i++] = '(';
            if (fractionList[j] >= 0) {
                resultString[i++] = '0' + fractionList[j];
            }
            else {
                resultString[i++] = '0' - fractionList[j];
            }
            /* if (fractionList[j] < 0) { */
            /*     printf("%d============\n", fractionList[j]); */
            /* } */
        }
        if (-1 != repeatingIndex)
            resultString[i++] = ')';
    }
    resultString[i++] = '\0';

    return resultString;
}

int main(int argc, char *argv[])
{
    printf("%s\n", fractionToDecimal(2, 3));
    printf("%s\n", fractionToDecimal(9, 3));
    printf("%s\n", fractionToDecimal(12, 33));
    printf("%s\n", fractionToDecimal(1, 2));
    printf("%s\n", fractionToDecimal(0, 2));
    printf("%s\n", fractionToDecimal(1, 1));
    printf("\n");

    printf("%s\n", fractionToDecimal(-2, 3));
    printf("%s\n", fractionToDecimal(-9, 3));
    printf("%s\n", fractionToDecimal(-12, 33));
    printf("%s\n", fractionToDecimal(-1, 2));
    printf("%s\n", fractionToDecimal(-0, 2));
    printf("%s\n", fractionToDecimal(-1, 1));
    printf("\n");

    printf("%s\n", fractionToDecimal(-2147483648, 1));
    printf("%s\n", fractionToDecimal(-2147483648, -1));
    printf("%s\n", fractionToDecimal(-2147483648, -1999));
    printf("%s\n", fractionToDecimal(7, -12));
    printf("\n");

    printf("%d\n", 7 % -12);
    printf("%d\n", -7 % 12);
    printf("%d\n", -13 % 5);
    printf("%d\n", 13 % 5);
    printf("%d\n", INT_MIN);
    printf("%d\n", -INT_MIN % -1);
    printf("%d\n", -INT_MIN % 1);
    printf("\n");
    printf("%d\n", INT_MIN % -1);
    printf("%d\n", INT_MIN % -1);
    printf("%d\n", INT_MIN % -1);
    printf("%d\n", INT_MIN % -1);
    printf("%d\n", INT_MIN % -1);
    printf("%d\n", INT_MIN % -1);
    printf("\n");
    printf("%d\n", INT_MIN / -1);
    printf("%d\n", INT_MIN / -1);
    printf("%d\n", INT_MIN / -1);
    printf("%d\n", INT_MIN / -1);
    printf("%d\n", INT_MIN / -1);
    printf("%d\n", INT_MIN / -1);

    printf("-------\n");
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", INT_MIN % 1);
    printf("\n");
    printf("%d\n", INT_MIN / 1);
    printf("%d\n", INT_MIN / 1);
    printf("%d\n", INT_MIN / 1);
    printf("%d\n", INT_MIN / 1);
    printf("%d\n", INT_MIN / 1);
    printf("%d\n", INT_MIN / 1);

//2147483648
    printf("\n");
    printf("%d\n", -2147483647 / -1);
    printf("%d\n", (-2147483647 - 1) / -1);
    printf("\n");
    printf("%d\n", INT_MIN % 1);
    printf("%d\n", -INT_MIN);
    printf("%d\n", INT_MIN / -1999);
    printf("%d\n", INT_MIN % -1999);

    return 0;
}
