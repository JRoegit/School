#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "arr.h"

/*
 * Reads count int values from f storing the values in 
 * the specified array.
 *
 * Does not close the file f.
 */
void arr_readn(FILE *f, size_t count, int *arr) {
    for(int i = 0;i < count; i++){
        *(arr + i) = fscanf(f,"%i");
    }
}


/*
 * Reads characters from f storing the characters in the array 
 * pointed at by s. Stops reading when a newline character '\n' 
 * is reached, or when max_length characters are read. A newline
 * character is never stored in the array pointed at by s.
 * A null terminator is always stored to indicate the end of the
 * string.
 *
 * Returns true if a newline character is reached (indicating
 * that an entire line of the file was read). Returns false
 * if the last character read was not the newline character,
 * or if reading from the file failed for some reason.
 *
 * Does not close the file f.
 */
bool arr_readline(FILE *f, size_t max_length, char *s) {
    for(int i = 0; i < max_length; i++){
        int current = fgetc(f);
        if(current == '\n'){
            return true;
        }
        *(s + i) = current;
        if((i == max_length - 1) && (current != '\n')){
            return false;
        }
    }
}


/*
 * Extracts integer values from a string where the integer values
 * are separated from one another by a single comma (no spaces).
 * The integer values are returned in a newly allocated array
 * having capacity exactly equal to the number of integers extracted.
 * The number of extracted integers is written into the object
 * pointed at by n.
 */
int *arr_fromstr(const char *s, size_t *n) {
    char *current = strtok(s,",");
    size_t count = 1;
    while(current != NULL){
        current = strtok(s,",");
        count++;
    }

    int *arr = malloc(count*sizeof(int));
    *n = count;

    char *newCurrent = strtok(s,",");
    count = 0;
    while(newCurrent != NULL){
        *(arr + count) = atoi(*newCurrent);
        count++;
        newCurrent = strtok(s,",");
    }

    return arr;
}





/*
 * Uncompresses the n element compressed array enc returning
 * a pointer to the first element of a new array
 * containing the uncompressed array. Writes the length of the
 * uncompressed array into the object pointed at by dec_len.
 *
 * The returned array has no excess capacity (i.e.,
 * all values in the returned array are meaningful).
 */
int *arr_decode(size_t n, const int *enc, size_t *dec_len) {
    size_t count = 0;
    for(int i = 0; i < n; i+=2){
        count += enc[i];
    }

    int *arr = malloc(count*sizeof(int));
    *dec_len = count;
    count=0;
    for(int i = 0;i < n; i+=2){
        for(int j = 0; j < enc[i]; j++){
            arr[count] = enc[i+1]; 
            count++;
        }
    }

    return arr;
}


