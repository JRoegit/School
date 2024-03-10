#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct point2 {
    double x;
    double y;
};

int main(int argc, char *argv[]){
    struct point2 *p;
    p = malloc(sizeof(struct point2));
    p->x = 1.0;
    p->y = 2.2;

    printf("%f",p->x);
    
    free(p);
    return 0;
}