#include <stdio.h>
#include <assert.h>
#include <ctype.h>

long long int my_atoi(const char *c)
{
    long long int value = 0;
    int sign = 1;
    if( *c == '+' || *c == '-' )
    {
        if( *c == '-' ) sign = -1;
        c++;
    }
    while (isdigit(*c))
    {
        value *= 10;
        value += (int) (*c-'0');
        c++;
    }
    return (value * sign);
}

int main(void)
{
    assert(5 == my_atoi("5"));
    assert(-2 == my_atoi("-2"));
    assert(-1098273980709871235 == my_atoi("-1098273980709871235"));
    puts("All good."); // I reach this statement on my system
    long long int test = 0;
    long int test2 = 0;
    int test3 = 0;
    //puts(sizeof test);
    printf("%d\n", sizeof test);
    printf("%d\n", sizeof test2);
    printf("%d\n", sizeof test3);
    printf("%u\n", 0xffffffffffffffff);
    printf("%lu\n", 0xffffffffffffffff);
    printf("%ld\n", 0x7fffffffffffffff);
    printf("%d\n", 0x7fffffffffffffff);
    printf("%d\n", 0x7fffffff);
    printf("%d\n", 0x7fff);
    printf("%u\n", 0xffff);
    printf("%ld\n", -1098273980709871235);

}
