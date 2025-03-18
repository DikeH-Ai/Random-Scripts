from itertools import groupby


def main(string: str) -> None:
    for key, group in groupby(string, key=None):
        print(f"({len(list(group))}, {key})", end=" ")


if __name__ == "__main__":
    string = input()
    main(string)
