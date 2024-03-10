#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int divide(int x, int y, int *rem, double *quot) {
    *quot = (double)x / (double)y;
    *rem = x % y; 
    return x / y;
}

int main(int argc, char *argv[]){
    if (argc != 3){
        fprintf(stderr, "Usage: divide int1 int2\n");
        return 1;
    };

    int val1 = atoi(argv[1]);
    int val2 = atoi(argv[2]);
    int rem;
    double quot;
    int division = divide(val1, val2, &rem, &quot);
    printf("%4d rem %4d \n%8.3f\n", division, rem, quot);
    return 0;
}