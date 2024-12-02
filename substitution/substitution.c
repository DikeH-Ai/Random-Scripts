#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

char substitute(char c, string key);

int main(int argc, string argv[])
{
    string key = argv[1];
//make sure the user inputs one argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
//make sure the key contains 26 letters
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0, len = strlen(key); i < len ; i++)
    {
//check for invalide characters
        if (!isalpha(key[i]))
        {
            return 1;
        }
//checks for duplicate characters
        for (int j = i + 1; j < len; j++)
        {
            if (key[i] == key[j])
            {
                return 1;
            }
        }
    }
    string plaintext = get_string("plaintext: ");
//print the cipher
    printf("ciphertext: ");
//ilterate through all the characters of plaintext
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
//call the substitute function
        char value = substitute(plaintext[i], key);
        printf("%c", value);
    }
    printf("\n");
    return 0;

}
//substitute function
char substitute(char c, string key)
{
//check char case & if its an alphabet
    if (isupper(c) != 0 && isalpha(c) != 0)
    {
        int position = (c - 65) % 26;
        return toupper(key[position]);
    }
    else if (islower(c) != 0 && isalpha(c) != 0)
    {
        int position = (c - 'a') % 26;
        return tolower(key[position]);
    }
    else
    {
        return c;
    }
}