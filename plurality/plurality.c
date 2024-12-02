#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    for (int i = 0, len = candidate_count; i < len ; i++)
    {
//compare strings case-insensitively between the input and strut index for name
        if (strcasecmp(name, candidates[i].name) == 0)
        {
//increase candidates vote
            candidates[i].votes++;
            return true;
        }
    }

    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
//initialize winner & winner_name variable
    int winner = 0;
    string winner_name = "";
//loop through all the vote values and store the highest
//also store the hight vote name
    for (int i = 0 ; i < candidate_count; i++)
    {
        if (candidates[i].votes > candidates[i + 1].votes && candidates[i].votes > winner)
        {
            winner = candidates[i].votes;
            winner_name = candidates[i].name;
        }
    }
//now this was trick; i would have prefer to print this value within the second "for loop" below
//but i dont know why check50 wouldn't approve it.
    printf("%s", winner_name);
    printf("\n");
//loop to all the values for a similar highest vote & print it
    for (int i = 0 ; i < candidate_count; i++)
    {
        if (candidates[i].votes == winner && candidates[i].name != winner_name)
        {
//print out the candidates name
            printf("%s", candidates[i].name);
            printf("\n");

        }
    }

    return;
}