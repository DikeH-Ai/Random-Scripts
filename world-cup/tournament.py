# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    # assign commandline argument to variable
    file = sys.argv[1]
    with open(file) as text:
        # assign csv object to variable
        reader = csv.DictReader(text)
        # loop through the csv file convert ratings to int and update team list
        for team in reader:
            team["rating"] = int(team["rating"])
            teams.append(team)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    # iterate through the loop N times
    for i in range(N):
        # assign functions protuct to variable
        winner = simulate_tournament(teams)
        # using .get() create a new key map or update an already existing one
        # .get() reference: https://www.adamsmith.haus/python/answers/how-to-increment-a-value-in-a-dictionary-in-python#:~:text=Use%20dict.-,get()%20to%20increment%20a%20value%20in%20a%20dictionary,plus%20the%20result%20of%20dict.
        counts[winner] = counts.get(winner, 0) + 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    # create an infinte loop
    keepgoing = True
    while keepgoing:
        # call the simulate round function
        winner = simulate_round(teams)
        teams = winner
        # check if winnner = 1, return that winner
        if len(winner) == 1:
            return teams[0]["team"]
            keepgoing = False


if __name__ == "__main__":
    main()
