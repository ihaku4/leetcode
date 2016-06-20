#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int myCounter = 0;

int isPrime(int n);
int countPrimes(int n);
int isPrime2(int n, const int *primes, int count);

// https://leetcode.com/discuss/34622/my-c-solutions-in-44ms-time-nearly-o-n-and-space-nearly-o-n
    /*1. trick1 is to use square root of n.
     2.  trick2 is not to use non-prime numbers as the step
     3. trick3 is to use i*i as the start. 
     4. trick4 is to use count-- in every loop, avoiding another traversal. */  
int countPrimes_from_leetcode(int n) {
    if(n <= 2) return 0;
    if(n == 3) return 1;
    bool *prime= (bool*)malloc(sizeof(bool)*n);
    int i=0,j=0;
    int count = n-2;
    int rt = sqrt(n);//trick1
    for(j = 0; j < n; j++)
    {
        prime[j] = 1;
    }
    for(i = 2; i <= rt; i++)
    {
         if (prime[i])//trick2
        {
            for(j=i*i ; j<n ; j+=i)//trick3
            {
                if (prime[j])
                        {
                           prime[j]=0;
                           count--;//trick4
                        }
            }
        }
    }
    free(prime);
    return count;
}


int isPrime2(int n, const int *primes, int count) {
    int i;
    
    for (i = 0; i < count && primes[i] * primes[i] <= n; i++) {
        myCounter++;
        if (n % primes[i] == 0) {
            return 0;
        }
    }
    return 1;
}

int isPrime(int n) {
    int i;

    for (i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int countPrimes(int n) {
    int i, count = 0;
    int *primes;

    primes = malloc(sizeof(int) * n);

    for (i = 2; i < n; i++) {
        if (isPrime2(i, primes, count)) {
        /* if (isPrime(i)) { */
            primes[count] = i;
            ++count;
        }
    }

    free(primes);
    return count;
}

int countPrimes2(int n) {
    int i, j, count = 0;
    int *isPrime;
    int sqrtN = sqrt(n);

    isPrime = malloc(sizeof(int) * n);

    for (i = 0; i < n; i++) {
        isPrime[i] = 1;
    }

    for (i = 2; i <= sqrtN; i++) {
        if (isPrime[i]) {
            for (j = i * i; j < n; j += i) {
                isPrime[j] = 0;
                myCounter++;
            }
        }
    }

    for (i = 2; i < n; i++) {
        if (isPrime[i])
            ++count;
    }

    free(isPrime);
    return count;
}

int main(int argc, char *argv[])
{
    printf("%d\n", countPrimes(10));
    printf("%d\n", myCounter);
    myCounter = 0;
    printf("%d\n", countPrimes(1500000));
    printf("%d\n", myCounter);

    myCounter = 0;
    printf("%d\n", countPrimes2(1500000));
    printf("%d\n", myCounter);
    return 0;
}
