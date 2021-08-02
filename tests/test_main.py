import lib.math as math


def test_add_two():
    assert math.add_two(1,2) == 3

def test_sub_two():
    assert math.sub_two(2,1) == 1

def test_div_two():
    assert math.div_two(2,2) == 1

def test_printeger():
    assert math.printeger(1) == "1"

