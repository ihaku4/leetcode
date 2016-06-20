#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isUgly2(int num) {
    int factors[] = {2, 3, 5};
    int i, len = 3;

    for (i = 0; i < len; i++)
        while (0 == num % factors[i])
            num /= factors[i];
    return 1 == num;
}

bool isUgly(int num) {
    if (0 == num) return false;
    while (0 == num % 2) num /= 2;
    while (0 == num % 3) num /= 3;
    while (0 == num % 5) num /= 5;
    return 1 == num;
}

int main(int argc, char *argv[])
{
    printf("%d\n", isUgly(19));
    printf("%d\n", isUgly(6));
    printf("%d\n", isUgly(8));
    printf("%d\n", isUgly(14));
    return 0;
}
