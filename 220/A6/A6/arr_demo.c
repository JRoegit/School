#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "arr.h"

int main(int argc, char *argv[]){
    if(argc > 2){
        fprintf(stderr, "Too many arguments.\nUsage: arr.c filename");
        return 1;
    }

    FILE *fo = fopen(argv[1],"r");
    if(fo == NULL){
        fprintf(stderr, "Could not read given filename.\nUsage: arr.c filename");
        return 2;
    }
    int *tmp = malloc(sizeof(int));
    arr_readn(fo,1,tmp);
    size_t lines = tmp[0];
    
    char temp[10];
    fgets(temp,10,fo);

    for(int i = 0;i < lines; i++){
        char *arr = malloc(100*sizeof(char));
        arr_readline(fo,100,arr);
        size_t *size;
        size_t *dec_len;
        int *decoded = arr_decode(*size,arr_fromstr(arr,size),dec_len);
        for(int i = 0;i < *dec_len; i++){
            if(decoded[i] == 1){
                printf("#");
            }
            else if(decoded[i] == 0){
                printf(" ");
            }
            printf("\n");
        }
        free(arr);
        free(decoded);
    }
    
    fclose(fo);
    return 0;
}
