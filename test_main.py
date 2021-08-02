import main


def test_add_two():
    assert main.add_two(1,2) == 3

def test_sub_two():
    assert main.sub_two(2,1) == 1

def test_div_two():
    assert main.div_two(2,2) == 1

def test_printeger():
    assert main.printeger(1) == "1"

