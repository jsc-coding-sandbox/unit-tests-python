import main


def test_add_two():
    assert main.add_two(1,2) == 3, "Should be 3"

def test_sub_two():
    assert main.sub_two(2,1) == 1, "Should be 1"

def test_div_two():
    assert main.div_two(2,2) == 1, "Should be 1"

def printeger():
    assert main.printeger(1) == "1", "Should be 1"


if __name__ == "__main__":
    test_add_two()
    test_sub_two()
    test_div_two()
    printeger()
    print("All passed!")
