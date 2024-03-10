#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "stack_utils.h"


void print_int(const void *elem) {
    int val = *((int *) elem);
    printf("%d", val);
}

int main(void) {
    stack *s = stack_init_empty();

    int *arr = malloc(3 * sizeof(int));
    arr[0] = 3;
    arr[1] = 4;
    arr[2] = 5;

    stack_push(s, arr);
    stack_push(s, arr + 1);
    stack_push(s, arr + 2);
    stack_print(s, print_int);

    free(arr);
    stack_free(s, NULL);

    return 0;
}