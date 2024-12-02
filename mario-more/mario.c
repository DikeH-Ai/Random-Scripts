#include <cs50.h>
#include <stdio.h>

int main(void)
{
//Initialize a variable
    int x;
//Request & validate user-input
    do
    {
        x = get_int("INPUT HEIGHT: ");
    }
    while ((x <= 0) || (x >= 9));
//Create pyramid
    for (int i = 1; i <= x; i++)
    {
//Right align pyramid
        for (int k = x; k > i; k--)
        {
            printf(" ");
        }
//Print pyramid
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
//Print gaps
        printf("  ");
//Print Left aligned pyramid
        for (int l = 0; l < i; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}