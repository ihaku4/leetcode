#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

char* reverseVowels(char* s) {
    char *vowels = "aeiouAEIOU";
    int len = strlen(s);
    int hi = len - 1, lo = 0;

    while (lo < hi) {
        while (lo < hi && NULL == strchr(vowels, s[lo]))
            ++lo;
        while (lo < hi && NULL == strchr(vowels, s[hi]))
            --hi;
        if (lo < hi) {  // swap s[lo], s[hi]
            s[lo] ^= s[hi];
            s[hi] ^= s[lo];
            s[lo] = s[lo] ^ s[hi];

            ++lo;
            --hi;
        }
    }
    return s;
}

int main(int argc, char *argv[])
{
    char a = 'a', b = 'b';
    char s[] = "leetcode";

    a ^= b;
    b ^= a;
    a = a ^ b;
    printf("%c %c\n", a, b);

    printf("%s\n", reverseVowels(s));
    printf("%s\n", reverseVowels("leetcode"));
    return 0;
}
