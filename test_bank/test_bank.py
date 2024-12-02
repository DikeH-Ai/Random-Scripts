from bank import value
import pytest
def test_hello():
    assert value("hello") == 0

def test_startswithH():
    assert value("hi") == 20

def test_incorrectvalues():
    assert value("Whatsup") == 100

def test_nothing():
    assert value("") == 100

def test_incorrectvalues():
    with pytest.raises(AttributeError):
        assert value(15236)

def test_caseinsensitivity():
    assert value("HELLO") == 0
