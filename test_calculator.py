import calculator


def test_addition():
    assert calculator.calculate('2 + 3') == 5


def test_subtraction():
    assert calculator.calculate('10 - 4') == 6


def test_multiplication():
    assert calculator.calculate('6 * 7') == 42


def test_division():
    assert calculator.calculate('8 / 2') == 4


def test_precedence():
    assert calculator.calculate('2 + 3 * 4') == 14

