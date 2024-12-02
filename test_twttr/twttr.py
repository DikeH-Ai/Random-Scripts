def main():
    words = input("Words: ").strip()
    print(shorten(words))


def shorten(word):
    result = ""
    for i in word:
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            result += i
    return result



if __name__ == "__main__":
    main()