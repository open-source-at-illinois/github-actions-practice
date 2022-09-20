import calculator

def test_addition():
    assert 7 == calculator.addition(3, 4)

def test_multiplication():
    assert 12 == calculator.multiplication(3, 4)

def test_division():
    assert 0.75 == calculator.division(3, 4)