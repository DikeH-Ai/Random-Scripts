import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("2/0")

    with pytest.raises(ValueError):
        assert fuel.convert("12/2")
        assert fuel.convert("s/t")

def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
