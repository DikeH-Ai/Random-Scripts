from twttr import shorten
import pytest

def test_words():
    assert shorten("nerve") == "nrv"
    assert shorten("process") == "prcss"
    assert shorten("forestry") == "frstry"

def test_numbers():
    with pytest.raises(TypeError):
        shorten(53)

def test_capitalvowel():
    assert shorten("DANCE") == "DNC"
    assert shorten("strIdE") == "strd"
    assert shorten("SEPARATE") == "SPRT"

def test_ommitnumbers():
    assert shorten("code8") == "cd8"
    assert shorten("render9") == "rndr9"

def test_ommitpunc():
    assert shorten("there's a way") == "thr's  wy"
    assert shorten("yes, he did") == "ys, h dd"