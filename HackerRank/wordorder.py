def main(word_list: dict) -> None:
    print(len(word_list))
    for key, value in word_list.items():
        print(value, end=" ")


if __name__ == "__main__":
    n = int(input())
    word_list = {}
    for _ in range(n):
        word = input()
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

    main(word_list)
