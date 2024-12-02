#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


int count_words(string text);

int main(void)
{
    string text = get_string("Text: ");
    count_words(text);
}

int count_words(string text)
{
    int countwords = 0;
    int len = strlen(text);
    for (int i = 0; i <= len; i++)
    {
        if (text[i] == ' ')
        {
            countwords++;
        }
    }
    printf("%i", countwords);

    return countwords;
}