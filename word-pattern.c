#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool wordPattern(char* pattern, char* str) {
    char *tokens['z'-'a'+1];
    char *sub;
    char *brkb;
    char *sep = " ";
    char *tofree, *string, *substring;
    int i;
    int result = 1;
    
    memset(tokens, 0, 'z'-'a'+1);

    /* tofree = string = strdup(str); */
    tofree = string = malloc(sizeof(char) * (strlen(str) + 1));
    strncpy(string, str, strlen(str)+1);
    string[strlen(str)] = '\0';
    /* printf("%s\n", string); */
    /* printf("------ %d\n", strlen(str)); */

    /* while ((sub = strsep(&string, sep)) != NULL) */
    for (sub = strtok_r(string, sep, &brkb), i = 0;
         sub && i < strlen(pattern);
         sub = strtok_r(NULL, sep, &brkb), i++)
    {
        /* printf("%s\n", sub); */
        /* printf("%s\n", tokens[pattern[i] - 'a']); */
        if ((substring = tokens[pattern[i] - 'a'])) {
            if (strcmp(substring, sub) != 0) {
                result = 0;
                break;
            }
        }
        else {
            tokens[pattern[i] - 'a'] = sub;
        }
    }

    free(tofree);
    return result;
}

int main(int argc, char *argv[])
{
    bool res;

    /* printf("%d\n", 'z'-'a'+1); */
    res = wordPattern("aba", "is kk is");
    printf("%d\n", res);
    res = wordPattern("deadbeef", "d e a d b e e f");
    printf("%d\n", res);
    res = wordPattern("abba", "dog cat cat fish");
    printf("%d\n", res);
    return 0;
}
