#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isHappy(int n) {
    int digit, sum = 0;
    int results[100];
    int resultCount = 0;
    int i;

    while (1) {
        for (sum = 0; n; n /= 10)
            sum += (n % 10) * (n % 10);
        if (sum == 1) {
            return true;
        } else {
            for (i = 0; i < resultCount; i++) {
                if (results[i] == sum) {
                    return false;
                }
            }
            n = sum;
            results[resultCount] = sum;
            ++resultCount;
        }
    }
}

int main(int argc, char *argv[])
{
    printf("%d\n", isHappy(19));
    return 0;
}
