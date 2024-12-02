#include <cs50.h>
#include <stdio.h>
#include <strings.h>
#include <math.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO
//loop through all the candidates
    for (int i = 0 ; i < candidate_count; i++)
    {
//compare each current candidate in loop to user input
        if (strcasecmp(candidates[i].name, name) == 0)
        {
//if strcasecmp is 0 then we can update the rank based on the current voter
            preferences[voter][rank] = i;
            return true;
        }
    }
//if non of the above condition works just return false
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    int rank = 0;
//create a loop i that ilterates through the totall nummber of voters
    for (int i = 0 ; i < voter_count; i++)
    {
//create a nested loop j that ilterates through the candidates
        for (int j = 0 ; j < candidate_count; j++)
        {
//if the jth candidate == voter prefernce[i][j] and candidate.elimination is false
            if (preferences[i][rank] == j && candidates[j].eliminated == false)
            {
//increase the candidates votes
                candidates[j].votes++;
                break;
            }
            else if (preferences[i][rank] == j && candidates[j].eliminated == true)
            {
                candidates[rank + 1].votes++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
//create a loop to loop through all the candidate votes
    for (int i = 0; i < candidate_count; i++)
    {
//if any of the candidate votes is > pass
        if (candidates[i].votes > voter_count / 2)
        {
//print that candidate as winner and return true
            printf("%s", candidates[i].name);
            printf("\n");
            return true;
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    int realsmallest;
//create a loop to loop through all the candidate votes
    for (int i = 0; i < candidate_count; i++)
    {
//equate the vote to a variable smallest
        int smallest = candidates[i].votes;
//if candidate vote < smallest, update it
        if (candidates[i].votes <= smallest && candidates[i].eliminated == false)
        {
            realsmallest = candidates[i].votes;
        }
    }

    return realsmallest;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
//define not tie
    int not_tie = 0;
//create a loop to loop through all the candidates
    for (int i = 0 ; i < candidate_count; i++)
    {
//if the candidates.votes != the min
        if (candidates[i].votes != min && candidates[i].eliminated == false)
        {
//increase not_tie by one
            not_tie++;
        }
    }
    if (not_tie == 0)
    {
        return true;
    }
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
//create a loop to loop through all the candidates
    for (int i = 0 ; i < candidate_count; i++)
    {
//if the candidate vote is equal to the min
        if (candidates[i].votes == min && candidates[i].eliminated == false)
        {
//change the value of candidate[i].elimination to true
            candidates[i].eliminated = true;
        }
    }
    return;
}