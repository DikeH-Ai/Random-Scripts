"""
    Replace data in clipboard with email and phone number
"""
import pyperclip
import re


def get_clip_data() -> str:
    return pyperclip.paste()


def parser(data: str) -> str:
    # use regex to search for numbers and emails
    # create numbersRegxobj
    number_emailRegexobj = re.compile(
        r"(?:(?:[\+0]?\d+|\+\d[\s](?:\(\d{3}\)))(?:[\s\.\-]\d+){1,4})|\w+@[a-zA-Z0-9]+\.[a-zA-z]{2,3}")
    match_list = number_emailRegexobj.findall(data)
    match_str = "\n".join(match_list)

    return match_str


def past_cl_data(cl_data: str):
    pyperclip.copy(cl_data)


if __name__ == "__main__":
    # access and return clipboard data
    data = get_clip_data()
    # clean data/ exctract numbers and emails
    cd_data = parser(data)
    # paste clean data to clipboard
    past_cl_data(cd_data)
