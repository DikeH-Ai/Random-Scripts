// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <cs50.h>
#include <math.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
//9067 is derived from the multiplication of [LENGHT] and [sum of all Alphabet ASCI values]
const unsigned int N = 90675;

// Hash table
node *table[N];
// create counter
int counter = 0;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //variable for hash function
    int hashed = hash(word);
    //create node pointer
    node *checker;
    checker = table[hashed];
    while (checker != NULL)
    {
        //compare strings
        if (strcasecmp(checker->word, word) == 0)
        {
            return true;
        }
        checker = checker->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //variables for the lenght of the string
    int n = strlen(word);
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        //add all the ASCII values of the word and return a lower case
        sum += toupper(word[i]);
    }
    //return the remainder of N and sum
    return round(N % sum);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //open dictionary file
    FILE *file = fopen(dictionary, "r+");
    if (file == NULL)
    {
        return false;
    }
    //create a buffer array to store variables
    char buffer[LENGTH + 1];
    //read strings from the file
    while (fscanf(file, "%s", buffer) != EOF)
    {
        //create node
        node *new_word = malloc(sizeof(node));
        if (new_word == NULL)
        {
            return false;
        }
        //copy buffer into node->word
        strcpy(new_word->word, buffer);
        int rnumb = hash(new_word->word);
        new_word->next = NULL;
        if (table[rnumb] == NULL)
        {
            //ppoint the intial pointer to node
            table[rnumb] = new_word;
            //increase counter for size function
            counter++;
        }
        else
        {
            //point node->next to intial node then point intial node to current node
            new_word->next = table[rnumb];
            table[rnumb] = new_word;
            counter++;
        }
    }
    fclose(file);
    //check
    if (counter >= 24)
    {
        return true;
    }
    else
    {
        return true;
    }

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //loop through the array of nodes
    for (int i = 0; i < (N - 1); i++)
    {
        //create two node pointers
        node *unloader, *temp;
        unloader = table[i];
        while (unloader != NULL)
        {
            temp = unloader;
            unloader = unloader->next;
            free(temp);
        }
    }
    return true;
}
