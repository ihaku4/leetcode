#include <stdio.h>
#include <stdlib.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    int i;

    for (i = 0; i < 32; i++) {
        if (n & 0x1 << i)
            result |= 0x1 << 31-i;
        else
            result &= 0xffffffff ^ 0x1 << 31-i;
    }
    return result;
}

uint32_t reverseBits2(uint32_t n) {
    int i;

    for (i = 0; i < 32/2; i++) {
        if ((n & 0x1 << i) ^ ((n & 0x1 << 31-i) >> 31-2*i))
            n ^= 0x1 << i | 0x1 << 31-i;
    }
    return n;
}

uint32_t reverseBits3(uint32_t n) {
    n = (n >> 16) | (n << 16);
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
    return n;
}

void printBit(uint32_t n) {
    int i;

    for (i = 0; i < 32; i++) {
        if (n & 0x1 << 31 - i) printf("1");
        else                   printf("0");
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    reverseBits(123);
    printBit(123);
    printBit(reverseBits(123));
    printBit(43261596);
    printBit(reverseBits(43261596));
    printf("00000010100101000001111010011100\n");
    printf("%d\n964176192\n", reverseBits(43261596));

    reverseBits2(123);
    printBit(123);
    printBit(reverseBits2(123));
    printBit(43261596);
    printBit(reverseBits2(43261596));
    printf("00000010100101000001111010011100\n");
    printf("%d\n964176192\n", reverseBits2(43261596));

    reverseBits3(123);
    printBit(123);
    printBit(reverseBits3(123));
    printBit(43261596);
    printBit(reverseBits3(43261596));
    printf("00000010100101000001111010011100\n");
    printf("%d\n964176192\n", reverseBits3(43261596));
    return 0;
}
