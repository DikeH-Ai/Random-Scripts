def main():
    words =  input("Input a text: ")
    new_word = convert(words)
    print(new_word)

def convert(words):
    words =  words.replace(":)","🙂").replace(":(","🙁")
    return words

main()