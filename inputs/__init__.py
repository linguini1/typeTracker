# Functions for taking user input
__author__ = "Matteo Golin"

# Imports
import argparse
from tools.constants import X_OPTIONS, Y_OPTIONS
from tools.display import console_display_choices


# Custom class error
class ValidateXY(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        x, y = values

        if X_OPTIONS[x] == Y_OPTIONS[y]:
            print(f"Got values {values}")
            raise ValueError("X and Y values cannot map to the same data!")
        setattr(namespace, self.dest, values)


# Set up command line arguments
command_line_desc = """Empty description."""
help_desc = """Takes an index for an X and Y argument to be plotted."""
parser = argparse.ArgumentParser(description=command_line_desc)

parser.add_argument(
    "-xy",
    help=help_desc,
    nargs=2,
    metavar=("X", "Y"),
    type=int,
    action=ValidateXY
    )


# Getting desired values
def get_x_y_value(choices: dict, x_or_y: str) -> int:
    """Returns a valid user choice for the desired x value to be plotted."""

    choice = input(f"Please input the desired value {x_or_y} to plot: ")

    keys_as_strings = [str(key) for key in choices]

    while choice not in keys_as_strings:
        print("That is not an option.")
        choice = input(f"Please input the desired {x_or_y} value to plot: ")

    return int(choice)


# Getting desired X and Y values
def get_user_choice() -> tuple[str, str]:

    """Returns the headers for the x and y value choices as a tuple."""

    # X
    console_display_choices(X_OPTIONS, "X")
    x_choice = get_x_y_value(X_OPTIONS, "X")

    # Y
    console_display_choices(Y_OPTIONS, "Y")
    y_choice = get_x_y_value(Y_OPTIONS, "Y")

    return X_OPTIONS[x_choice], Y_OPTIONS[y_choice]
