#include<string.h>
#include<stdio.h>

int lengthOfLongestSubstring(char *s);

int main(void)
{
  printf("max length: %d\n", lengthOfLongestSubstring("aaaaaab"));
  printf("max length: %d\n", lengthOfLongestSubstring("aaaaaaa"));
  printf("max length: %d\n", lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "));
  printf("max length: %d\n", lengthOfLongestSubstring("c"));
  printf("max length: %d\n", lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "));
  printf("max length: %d\n", lengthOfLongestSubstring("c"));
  //printf("%x\n", 989877440);
  //printf("%d\n", 989877440);
  //printf("%d\n", 0xffffffff);
  //printf("%d\n", 0x7fffffff);
  //printf("%d\n", 0x80000000);
  return 0;
}

int lengthOfLongestSubstring(char *s) {
  int cur_sub_start = 0;
  int max_sub_len = 0;
  int i;
  int last_pos_of_char[256];

  memset(last_pos_of_char, -1, 256 * sizeof(int));
  for (i = 0; s[i]; i++) {
    if (last_pos_of_char[s[i]] < cur_sub_start)
      max_sub_len = max_sub_len > i - cur_sub_start + 1 ?
                    max_sub_len : i - cur_sub_start + 1;
    else
      cur_sub_start = last_pos_of_char[s[i]] + 1;
    last_pos_of_char[s[i]] = i;
  }
  return max_sub_len;
}
