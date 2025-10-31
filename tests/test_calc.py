from src.calc import add, mul, sub

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(4, 5) == 20

def test_sub():
    assert sub(10, 3) == 7
