#include <stdio.h>

int main ()
{
    int x = 66;
    int *p = &x;
    int **t = &p;
    printf("p  = %i, *t = %i", sizeof(p), sizeof(*t));
    return 0;
}