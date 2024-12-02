from plates import is_valid


def test_lenghtcheck():
    assert is_valid("C") == False

def test_middlecheck():
    assert is_valid("AA5AA") == False
    assert is_valid("CS05") == False

def test_aplhacheck():
    assert is_valid("55505") == False

def test_alphanumericcheck():
    assert is_valid("CS''50") == False
    assert is_valid("CS50") == True