#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "list_utils.h"


int main(void) {
    list *t = list_init_empty();
    list *a = list_init_empty();
    
    list_add(a,-3);
    list_add(a,-4);
    list_add(a,-5);

    list_add(t, 0);
    list_add(t, 1);
    list_add(t, 2);
    list_add(t, 3);
    list_add(t, 4);
    list_add(t, 5);
    list_add(t, 6);
    list_add(t, 7);
    list_add(t, 8);
    list_add(t, 9);

    list_insert_all(t,5,a);

    list_print(t);
    list_free(t);

    return 0;
}