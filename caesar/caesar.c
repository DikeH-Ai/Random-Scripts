#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string num);
char rotate(char letter, int position);

int main(int argc, string argv[])
{
//initiating argv to a variable
    string num = argv[1];
//check if program runs with one argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
//check if argument is a digit although its in a string format
    bool dec = only_digits(num);
    if (dec == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
//convert string to an int
    int conv = atoi(num);
//request for value of plaintext
    string plaintext = get_string("plaintext:  ");
//print the cipher
    printf("ciphertext: ");
//ilterate through all the characters of plaintext
    for (int i = 0, len = strlen(plaintext); i < len ; i ++)
    {
//call the rotate function
        char value = rotate(plaintext[i], conv);
        printf("%c", value);
    }
    printf("\n");
    return 0;
}
//funtion to check if command line argument is a digit
bool only_digits(string num)
{
    int len = strlen(num);
    for (int i = 0; i < len; i++)
    {
        if (!isdigit(num[i]))
        {
            return false;
        }

    }
    return true;
}

//rotate funtion
char rotate(char letter, int position)
{
//uppercase and lowercase alphabet arrays
    char uppercase[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char lowercase[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
//uppercase condition
    if (isalpha(letter) != 0 && isupper(letter) != 0)
    {
//used the Ci = (Pi + k)%26 hint from the example to get the index value 
        int new_letter = ((letter - 65) + position) % 26 ;
        return uppercase[new_letter];
    }
//lowercase condition
    else if (isalpha(letter) != 0 && islower(letter) != 0)
    {
        int new_letter = ((letter - 'a') + position) % 26;
        return lowercase[new_letter];
    }
    else
    {
        return letter;
    }

}

