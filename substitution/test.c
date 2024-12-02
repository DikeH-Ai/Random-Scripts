#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char c = 'B';
    string key = "YTNSHKVEFXRBAUQZCLWDMIPGJO";
    if((isupper(c) != 0) && isalpha(c) != 0)
    {
        int position = (c - 65) % 26;
        printf("%c \n", key[position]);
        return toupper(key[position]);
    }
}
