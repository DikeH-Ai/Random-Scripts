import pytest
from numb3rs import validate

def main():
    test_ip_range()
    test_wrong_ip()
    test_ip()


def test_ip_range():
    assert validate("256.256.22.2") == False
def test_wrong_ip():
    assert validate("25.321.6.28") == False
    assert validate("234.3.23.2.32") == False
def test_ip():
    assert validate("123.22.23.2") == True
    assert validate("-1.-1.0.1") == False


if __name__ == "__main__":
    main()