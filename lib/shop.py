"""
There's an issue with this - it prints \t and \n as literally "\t" and "\n"...
TODO: Fix it.
"""
def format_data_for_display(data: list):
    display = ""
    for item in data:
        display += (f"Product Name:\t{item.get('product_name')}\n"
                    + f"Price:\t{item.get('price')}\n"
                    + f"Type:\t{item.get('type')}\n"
                    + f"Company:\t{item.get('company')}\n"
                    )
    return display

def format_data_as_csv(data: list):
    pass
