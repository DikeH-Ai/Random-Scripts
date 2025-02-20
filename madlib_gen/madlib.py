def main():
    welcome()
    words = get_inputs()
    print(story(words))


def welcome():
    print("""Welcome to the Mad Libs Generator!
You will be asked for different words to create a funny story. Let's Go""")


def get_inputs():
    words = {
        "noun1": "Choose a noun: ",
        "pnoun": "Choose a plural noun: ",
        "noun2": "Choose another noun: ",
        "adjective": "Choose an adjective (a describing word): ",
        "place": "Name a place: ",
        "noun3": "Choose one more noun: "
    }
    return [input(value) for value in words.values()]


def story(words: list):
    return f""" 
    Be kind to your {words[0]}-footed {words[1]}
    For a duck may be somebody's {words[2]},
    Be kind to your {words[1]} in {words[3]}
    Where the weather is always {words[4]}.
    You may think that this is the {words[5]},
    Well it is."""


if __name__ == "__main__":
    main()
