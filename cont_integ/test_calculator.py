import calculator

def test_add():
    total=calculator.add(4,5)
    assert total==9
def test_subtract():
    total=calculator.subtract(9,5)
    assert total==4
def test_multiply():
    total=calculator.multiply(10,3)
    assert total==30
def test_divide():
    total=calculator.divide(9,3)
    assert total==3

