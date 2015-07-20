#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void
swap(char *c1, char *c2);
void
reverseString(char *s, long h, long t);
int
removeExtraSpacesBetweenWords(char *s, int len);
char *
reverseWords(char *s);

char *
reverseWords(char *s)
{
  int head = 0, t = 0;
  size_t l = strlen(s);
  t = l - 1;
  int hPre;
  int i, j;

  // Strip And Reverse
  while (t >= 0 && s[t] == ' ') s[t--] = '\0';
  reverseString(s, head, t);
  while (t >= 0 && s[t] == ' ') s[t--] = '\0';

  l = removeExtraSpacesBetweenWords(s, t + 1);
  t = l - 1;

  // Reverse Every Words
  while (head <= t) {
    while (head <= t && s[head] == ' ') head++;
    hPre = head;
    while (head <= t && s[head] != ' ') head++;
    if (hPre <= t) reverseString(s, hPre, head - 1);
  }

  return s;
}

int
removeExtraSpacesBetweenWords(char *s, int len)
{
  int i, j;
  int head, t;
  t = len - 1;

  // Clear Extra Spaces Between Words
  // Mark Extra Spaces to '\0'
  for (head = 0; head <= t; head++) {
    while (head <= t && s[head] != ' ') head++;
    while (head <= t && s[++head] == ' ') s[head] = '\0';
  }

  // Shift Non-space Characters
  i = 0;
  while (i <= t && s[i] != '\0') i++;
  for (j = i+1; j <= t; j++)
    if (s[j] != '\0')
      s[i++] = s[j];
  s[i] = '\0';
  return t + 1;
}

void
reverseString(char *s, long h, long t)
{
  while (h < t) swap(s+h++, s+t--);
}

void
swap(char *c1, char *c2)
{
  char swp;
  swp = *c1;
  *c1 = *c2;
  *c2 = swp;
}

int
main()
{
  //char* s = "Reverse Words In A String";
  //char* s = "";
  //char* s = "1 ";
  char* s = "   a   b ";
  //char[strlen(s) + 1] sCp;
  //char sCp[25];
  //char sCp[strlen(s)+1];  // How this works?
  char *sCp = malloc((strlen(s) + 1) * sizeof(char *));
  int i;

  //for (i = 0; *(sCp+i) = *(s+i); i++);
  printf("%lu\n", strlen(s));
  strcpy(sCp, s);
  printf("%s\n", sCp);
  reverseWords(sCp);
  //printf("%s\n", reverseWords(s));
  printf("%s------\n", sCp);
  return 0;
}
