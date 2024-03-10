#include <stdio.h>
#include <stdlib.h>

double med(double x, double y, double z){
    if ((x <= y && y <= z) || (z <= y && y <= x)) {
        return y;  
    } else if ((y <= x && x <= z) || (z <= x && x <= y)) {
        return x;
    } else {
        return z;
    }
}

int main(int argc, char *argv[]) {
    if (argc == 1){
        printf("0\n");
        return 0;
    }
    else if (argc != 4){
        return 1;
    }
  
    printf("%f\n", med(atof(argv[1]), atof(argv[2]), atof(argv[3])));
    return 0;
}