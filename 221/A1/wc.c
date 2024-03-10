#include <stdio.h>
#include <string.h>

int main() {
    int lines = 0, words = -1, chars = 0;
    char currentchar;

    printf("Enter text (Ctrl-D to end input):\n");

    while ((currentchar = getchar()) != EOF) {
        chars++;
        if (currentchar == '\n') {
            lines++;
        }

        if (currentchar == '\n' || currentchar == '\t' || currentchar == ' ') {
            while ((currentchar = getchar()) == '\n' || currentchar == '\t' || currentchar == ' ') {
                continue;
            }
            ungetc(currentchar, stdin);
            words++;
        }
    }

    if (chars > 0) {
        words++;
    }

    printf("\nWord Count: %d\n", words);
    printf("Line Count: %d\n", lines);
    printf("Character Count: %d\n", chars);

    return 0;
}
