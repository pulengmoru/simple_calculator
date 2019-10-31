from simple_calculator import add, multiply

def test_add():
    assert add(0,0) == 0

def test_add_negative_numbers():
    assert add(-1,-1) == -2

def test_add_different_numbers():
    assert add(4,5) == 9

def test_add_multiple_numbers():
    assert add(1,2,3,4) == 10    

def test_multiply():
    assert multiply(1,2) == 2

def test_multiply_multiple():
    assert multiply(1,2,3,4) == 24