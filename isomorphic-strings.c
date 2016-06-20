#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define LETTER_SIZE 256

bool isIsomorphic(char* s, char* t) {
    char used[LETTER_SIZE];
    bool mapped[LETTER_SIZE];
    int i, len;

    memset(used, 0, sizeof(char) * LETTER_SIZE);
    memset(mapped, 0, sizeof(bool) * LETTER_SIZE);

    for (i = 0, len = strlen(s); i < len; i++) {
        if (used[s[i]]) {
            if (used[s[i]] != t[i]) {
                return false;
            }
        }
        else if (mapped[t[i]]) {
            return false;
        }
        used[s[i]] = t[i];
        mapped[t[i]] = true;
    }
    return true;
}

int main(int argc, char *argv[])
{
    printf("%d\n", isIsomorphic("aabb", "ccdd"));
    printf("%d\n", isIsomorphic("aabb", "cccd"));
    printf("%d\n", isIsomorphic("ab", "cc"));
    printf("%d\n", isIsomorphic("13", "42"));
    return 0;
}
