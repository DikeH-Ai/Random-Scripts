def main():
    words = input("Words: ").strip()
    remove_vowel(words)

def remove_vowel(words):
    for i in words:
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            print(i, end="")
    print()

main()