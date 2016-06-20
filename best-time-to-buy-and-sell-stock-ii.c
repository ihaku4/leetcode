#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    int i;

    if (pricesSize < 2)
        return 0;

    for (i = 1; i < pricesSize; i++) {
        if (prices[i] > prices[i-1])
            profit += prices[i] - prices[i-1];
    }

    return profit;
}

int main(int argc, char *argv[])
{
    int prices[] = {1, 4, 2, 5, 6, 19, 10, 3, 9};
    int len = 9;

    printf("%d\n", maxProfit(prices, len));
    return 0;
}
