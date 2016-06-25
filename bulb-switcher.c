#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int bulbSwitch(int n) {
    return sqrt(n);
}

int bulbSwitch_slow(int n) {
    int step, i;
    int count = 0;
    int on = 1;

    if (0 > n) return -1;
    if (0 == n) return 0;

    count = 1;
    for (step = 2; step <= n; step++) {
        on = 0;
        for (i = 2; i <= step / 2; i++) {
            if (step % i == 0)
                on ^= 1;
        }
        count += on;
    }
    return count;
}

int main(int argc, char *argv[])
{
    printf("%d\n", bulbSwitch(3));
    printf("%d\n", bulbSwitch(999));
    return 0;
}
