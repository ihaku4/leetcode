#include <stdio.h>

// Forward declaration of isBadVersion API.
/* bool isBadVersion(int version); */
int isBadVersion(int version);
int isBadVersion(int version) {
    /* printf("version: %d\n", version); */
    if (version < 1702766719)   return 0;
    /* if (version < 1702766719)   return 1; */
    else                        return 1;
}

int firstBadVersion(int n) {
    int lo = 1, hi = n - 1;
    int mi;

    if (isBadVersion(1)) return 1;
    if (!isBadVersion(n)) return 0;

    while (lo <= hi) {
        mi = (lo >> 1) + (hi >> 1) + ((lo & 1) & (hi & 1));
        if      (isBadVersion(mi))
            hi = mi - 1;
        else if (!isBadVersion(mi) && !isBadVersion(mi+1))
            lo = mi + 1;
        else break;
    }
    return mi + 1;
}

int firstBadVersion2(int n) {
    int lo = 1, hi = n;
    int mi;

    while (lo < hi) {
        mi = (unsigned int) (lo + hi) >> 1;
        if (isBadVersion(mi)) hi = mi;
        else                  lo = mi + 1;
    }
    if (isBadVersion(lo)) return lo;
    else                  return 0;
}

int main(int argc, char *argv[])
{
    printf("%d\n", firstBadVersion(2126753390));
    printf("%d\n", firstBadVersion2(2126753390));
    return 0;
}

