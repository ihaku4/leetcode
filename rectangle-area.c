#include <stdio.h>
#include <stdlib.h>

#ifndef min
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#endif

#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif

/**
 *                                  (G,H)
 *          --------------------------
 *          |                        |
 *          |        (C,D)           |
 *      ----|---------               |
 *      |   |        |               |
 *      |   |        |               |
 *      |   ---------|----------------
 *      | (E,F)      |
 *      --------------
 *    (A,B)
 */
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    int Xmax, Xmin, Ymax, Ymin;
    int width, height;

    Xmax = min(C, G);
    Xmin = max(A, E);
    Ymax = min(D, H);
    Ymin = max(B, F);

    if (Xmax < 0 && Xmin > 0) {
        width = 0;
    } else {
        width = max(0, Xmax - Xmin);
    }
    if (Ymax < 0 && Ymin > 0) {
        height = 0;
    } else {
        height = max(0, Ymax - Ymin);
    }
    return (C - A) * (D - B) + (G - E) * (H - F) - width * height;
}

int main(int argc, char *argv[])
{
    printf("%d\n", computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
    printf("%d\n", computeArea(0, 0, 0, 0, -1, -1, 1, 1));
    printf("%d\n", computeArea(-1500000001, 0, -1500000000, 1, 1500000000, 0, 1500000001, 1));
    return 0;
}
