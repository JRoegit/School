#include <stdio.h>

int subtract2sc_issafe(int x, int y) {
    int result = x - y;
    if ((x >= 0 && y >= 0) || (x < 0 && y < 0)) { // compare signs of inputs
        if ((x >= 0 && result < 0) || (x < 0 && result >= 0)) { //overflow condition, compare signs of input to output
            return 0;
        }
    }
    return 1;
}