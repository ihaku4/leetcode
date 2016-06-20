#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool wordPattern2(char* pattern, char* str)
{
        int i, j, len = strlen(pattern);
        int search[len];
        char *token, *saveptr; char strtmp[strlen(str)];
        for(i = 0; i < len; i++) search[i] = -1;

        strcpy(strtmp, str);
        token = strtok_r(strtmp, " ", &saveptr);
        for(i = 0; i < len; i++)
        {
                int a = strchr(pattern, pattern[i]) - pattern;

                if(token == NULL) break;
                int b = strstr(str, token) - str;

                for(j = 0; j < a; j++)
                        if(search[j] == b) return false;
                if(search[a] == -1) search[a] = b;
                else if(search[a]!= b) return false;
                token = strtok_r(NULL, " ", &saveptr);
        }
        if((token == NULL) ^ (i== len)) return false;
        return true;
}

bool wordPattern(char* pattern, char* str) {
    char *tokens['z'-'a'+1];
    char *sub;
    char *brkb;
    char *sep = " ";
    char *tofree, *string, *substring;
    int i, j;
    int result = 1;
    bool stop = false;
    
    /* memset(tokens, 0, 'z'-'a'+1); */
    memset(tokens, 0, sizeof(char *) * ('z'-'a'+1));

    tofree = string = strdup(str);
    /* tofree = string = malloc(sizeof(char) * (strlen(str) + 1)); */
    /* strncpy(string, str, strlen(str)+1); */
    /* string[strlen(str)] = '\0'; */
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
                /* printf("%s\n", sub); */
                /* printf("%s\n", tokens[pattern[i] - 'a']); */
                result = 0;
                break;
            }
        }
        else {
            tokens[pattern[i] - 'a'] = sub;
        }
    }

    /* if ((NULL == sub && i < strlen(pattern)) || (sub && i >=strlen(pattern))) { */
    if ((NULL == sub) ^ (i == strlen(pattern))) {
        result = 0;
        stop = true;
    }
    for (i = 0; i <= 'z'-'a'; i++) {
        if (stop) break;
        for (j = i + 1; tokens[i] && tokens[j] && j <= 'z'-'a'; j++) {
            if (stop) break;
            if (strcmp(tokens[i], tokens[j]) == 0) {
                result = 0;
                stop = true;
                break;
            }
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
    res = wordPattern("abcdefghijklmnnmlkjihgfedcba",
                      "aa bb cc dd ee ff gg hh ii jj kk ll mm nn nn mm ll kk jj ii hh gg ff ee dd cc bb aa");
    printf("%d\n", res);
    res = wordPattern("abba", "aa aa aa aa");
    printf("%d\n", res);
    res = wordPattern("aaa", "aa aa aa aa");
    printf("%d\n", res);
    res = wordPattern("aaaaa", "aa aa aa aa");
    printf("%d\n", res);
    res = wordPattern2("abaa", "aaa aa aaa aaa");
    printf("%d\n", res);
    res = wordPattern("abaa", "aaa aa aaa aaa");
    printf("%d\n", res);
    return 0;
}
