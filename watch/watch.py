import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    result = re.search(r"src=\"https?:\/\/(www\.)?youtube.com\/embed\/(.+)\"",s)
    if result:
        return f"https://youtu.be/{result.group(2)}"

if __name__ == "__main__":
    main()