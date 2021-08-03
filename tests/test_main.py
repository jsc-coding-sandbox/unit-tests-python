import pytest
import lib.math as math
import lib.shop as shop


def test_add_two():
    assert math.add_two(1,2) == 3

def test_sub_two():
    assert math.sub_two(2,1) == 1

def test_div_two():
    assert math.div_two(2,2) == 1

def test_printeger():
    assert math.printeger(1) == "1"

@pytest.fixture
def example_product_data():
    return [
            {
                "product_name": "NiceApp",
                "price": 12.80,
                "type": "software",
                "company": "Nice Software Inc.",
            },
            {
                "product_name": "Generic AAA Game",
                "price": 50.99,
                "type": "game",
                "company": "Generic AAA Devs",
            },
        ]

def test_format_data_for_display(example_product_data):
    assert shop.format_data_for_display(example_product_data) == [
            "Product Name:\tNiceApp\n",
            "Price:\t12.80\n",
            "Type:\tsoftware\n",
            "Company:\tNice Software Inc.\n",
            "Product Name:\tGeneric AAA Game\n",
            "Price:\t50.99\n",
            "Type:\tgame\n",
            "Company:\tGeneric AAA Devs\n",
            ]
