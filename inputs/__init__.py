# Functions for taking user input
__author__ = "Matteo Golin"

# Imports
from typeTracker.tools.constants import X_OPTIONS, Y_OPTIONS
from typeTracker.tools.display import console_display_choices


# Getting desired values
def get_x_y_value(choices: dict, x_or_y: str) -> str:
    """Returns a valid user choice for the desired x value to be plotted."""

    choice = input(f"Please input the desired value {x_or_y} to plot: ")

    while choice not in choices.keys():
        print("That is not an option.")
        choice = input(f"Please input the desired {x_or_y} value to plot: ")

    return choice


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
