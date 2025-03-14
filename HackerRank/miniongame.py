# The Minion Game

def minion_game(word: str):
    word = word.lower()
    # get all subsets of the strings
    k = 0
    s = 0

    for i in range(len(word)):
        score = len(word) - i

        if word[i] in 'aeiou':
            k += score
        else:
            s += score

    if k != s:
        print(f"Stuart {s}") if s > k else print(f"Kevin {k}")
    else:
        print("Draw")


if __name__ == "__main__":
    minion_game(str(input("Word: ")))
