#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

char* getHint(char* secret, char* guess) {
    int secretCount[10];
    int guessCount[10];
    int i, len;
    int bull = 0, cow = 0;
    char *result;

    result = malloc(sizeof(char) * 100);
    memset(secretCount, 0, sizeof(int) * 10);
    memset(guessCount, 0, sizeof(int) * 10);

    for (i = 0, len = strlen(secret); i < len; i++) {
        ++secretCount[secret[i] - '0'];
        if (secret[i] == guess[i]) {
            ++guessCount[secret[i] - '0'];
            ++bull;
        }
    }
    for (i = 0, len = strlen(secret); i < len; i++) {
        if (secret[i] == guess[i]) {
            continue;
        }
        if (guessCount[guess[i] - '0'] < secretCount[guess[i] - '0']) {
             ++guessCount[guess[i] - '0'];
             ++cow;
        }
    }
    snprintf(result, 100, "%dA%dB", bull, cow);
    return result;
}

int main(int argc, char *argv[])
{
    printf("%s\n", getHint("1807", "7810"));
    printf("%s\n", getHint("1123", "0111"));
    printf("%s\n", getHint("11", "10"));
    return 0;
}
