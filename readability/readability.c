#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
//request for user input.
    string text = get_string("Text: ");
//lenght of the input.
    int len = strlen(text);
//call all functions.
    float L = count_letters(text);
    float W = count_words(text);
    float S = count_sentences(text);
//Coleman-Liau index
    L = (L / W) * 100;
    S = (S / W) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        //rounding the finial digit using code from math.h module
        printf("Grade %i\n", (int) round(index));
    }
}

//count letters function
int count_letters(string text)
{
    int count = 0;
    int len = strlen(text);
    for (int i = 0; i <= len; i++)
    {
        //for lowercase letters.
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            count++;
        }
        //for highercase letters.
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            count++;
        }
    }
    return count;
}
//count words function
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
//'couuntwords'seems to always be a digit behind so i added "+ 1"
    countwords = countwords + 1;
    return countwords;
}

//count sentences function
int count_sentences(string text)
{
    int countsent = 0;
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (text[i] == '.')
        {
            countsent++;
        }
        else if (text[i] == '!')
        {
            countsent++;
        }
        else if (text[i] == '?')
        {
            countsent++;
        }
    }
    return countsent;
}
