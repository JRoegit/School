#include <stdio.h>

/*
 * Prints the values of a on a single line with no space between
 * the values. Prints a newline character after printing all of
 * the array values.
 * 
 * Values are printed left to right starting from a[0] and ending with a[7].
 */
void print(int a[static 8]) {
    printf("%d%d%d%d%d%d%d%d\n",a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]);
}

/*
 * Translates a string str consisting of '0' and '1' characters
 * into an array bin consisting of 0 and 1 integer values. For
 * example, the string "00000001" results in the array bin
 * having the values bin[0] = 0, bin[1] = 0, ..., bin[7] = 1.
 */
void tobinary(char str[static 8], int bin[static 8]) {
    for (int i = 0; i < 8 ; i++){
        if (str[i] == '1'){
            bin[i] = 1;
        }
        else {
            bin[i] = 0;
        }
    }
}

/*
 * Sums the 8-digit binary values x and y storing the result
 * in z. The sum is computed using the standard long
 * addition algorithm from grade school.
 */
int sum(int x[static 8], int y[static 8], int z[static 8]) {
    int carry = 0;
    for (int i = 7; i > -1; i--){
        z[i] = 0;
        if(((x[i] == 1) && (y[i] == 0) && (carry == 0)) || ((x[i] == 0) && (y[i] == 1) && (carry == 0))){
            z[i] = 1;
            carry = 0;
        }
        else if(((x[i] == 1) && (y[i] == 1) && (carry == 0)) || ((x[i] == 1) && (y[i] == 0) && (carry == 1)) || ((x[i] == 0) && (y[i] == 1) && (carry == 1))){
            carry = 1;
        }
        else if((x[i] == 0) && (y[i] == 0) && (carry == 1)){
            z[i] = 1;
            carry = 0;
        }
        else if((x[i] == 1) && (y[i] == 1) && (carry == 1)){
            z[i] = 1;
            carry = 1;
        }
    }
    print(z);
    if (carry == 1){
        printf("overflow\n");
    }
    
}

int main(int argc, char *argv[]){
    if (argc != 3){
        return 1;  
    };

    int bin1[8];
    int bin2[8];
    int result[8];
    tobinary(argv[1], bin1);
    tobinary(argv[2], bin2);

    sum(bin1,bin2,result);
    return 0;
}