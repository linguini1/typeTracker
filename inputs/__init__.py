# Functions for taking user input
__author__ = "Matteo Golin"

# Imports
import argparse
from tools.constants import X_OPTIONS, Y_OPTIONS, ISO_PATTERN, MAX
from tools.display import console_display_choices


# Custom classes
class ValidateXY(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        x, y = values

        if X_OPTIONS[x] == Y_OPTIONS[y]:
            print(f"Got values {values}")
            raise ValueError("X and Y values cannot map to the same data!")
        setattr(namespace, self.dest, values)


class ValidateDeg(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        if not 1 <= values <= MAX:
            print(f"Got degree {values}")
            raise ValueError(f"Degree must be between 1 and {MAX}")
        setattr(namespace, self.dest, values)


class ValidateRange(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

        lower, upper = values

        if not (ISO_PATTERN.match(upper) and ISO_PATTERN.match(lower)):  # Must match specified date format
            print(f"Got start date {lower} and end date {upper}.")
            raise ValueError(f"Dates must be in format yyyy-mm-dd.")

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
    metavar="D",
    default=1,
    action=ValidateDeg
)

parser.add_argument(
    "-dr",
    help="Specifies the date range from which to pull data. Default shows all data points.",
    type=str,
    metavar=("Sd", "Ed"),
    default="all",
    nargs=2,
    action=ValidateRange
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


# Getting date range
def get_date_range(stats: dict) -> tuple[str, str] | str:

    # Prompt
    print("Please enter the range of dates you want to plot data from in the format: <Start Date>, <End Date>")
    print("Each individual date should be in the format yyyy-mm-dd (ex: 2021-01-01).")
    print("To use all available data points, please enter 'all'.")

    while True:

        user_range = input("Date range: ")

        if user_range.lower() == "all":  # All data points available to be used
            return user_range

        # Unpack input
        try:
            lower, upper = user_range.replace(" ", "").split(",")

            print(lower, upper)

            if ISO_PATTERN.match(upper) and ISO_PATTERN.match(lower):  # Must match specified date format

                if upper in stats.keys() or lower in stats.keys():
                    return lower, upper
                else:
                    print("At least one of your dates must be present in the dataset.")
            else:
                print("At least one of your dates was not in the right format of yyyy-mm-dd.")

        except ValueError:
            print("Make sure you've entered your dates in the format: <Start Date>, <End Date>")

