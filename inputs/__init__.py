# Functions for taking user input
__author__ = "Matteo Golin"

# Imports
import argparse
from tools.constants import X_OPTIONS, Y_OPTIONS
from tools.display import console_display_choices


# Custom classes
class ValidateXY(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        x, y = values

        if X_OPTIONS[x] == Y_OPTIONS[y]:
            print(f"Got values {values}")
            raise ValueError("X and Y values cannot map to the same data!")
        setattr(namespace, self.dest, values)


# Set up command line arguments
help_desc = "Takes an index for an X and Y argument to be plotted."  # Header for help description
parser = argparse.ArgumentParser()

parser.add_argument(  # X and Y values
    "-xy",
    help=help_desc,
    nargs=2,
    metavar=("X", "Y"),
    type=int,
    action=ValidateXY
    )

parser.add_argument(  # Option display
    "-options",
    help="Displays the list of options for X and Y values that can be plotted.",
    action="store_true"
    )

parser.add_argument(
    "-deg",
    help="Specifies the degree of the curve used to interpolate the data.",
    type=int,
    nargs=1,
    metavar="D",
    default=1
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


# Getting degree
def get_degree(n: int) -> int:

    MAX = 4  # Maximum degree for polynomial interpolation
    max_deg = min(MAX, n - 1)  # Max degree for polynomial interpolation based on number of data points (n - 1)

    while True:

        # Get degree
        degree = input(f"Degree of polynomial between 1 and {max_deg} used to interpolate the data: ")

        # Check if degree is an integer value
        try:
            degree = int(degree)
            is_int = True  # Integer
        except ValueError:
            is_int = False  # Not an integer
            print("The degree must be an integer.")

        # Check if degree is within the range of 1 - max_deg
        if is_int and (1 <= degree <= max_deg):
            break
        elif not is_int:
            pass
        else:
            print(f"The degree must be between 1 and {max_deg}.")

    return degree


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
