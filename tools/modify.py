# Functions for modifying data
__author__ = "Matteo Golin"

# Imports
import operator
from datetime import datetime, timedelta
from tools.constants import DATE_FORMAT, LESSON_LABELS, X_OPTIONS


# Modifying data
def convert_time_minutes(milliseconds: int) -> float:

    """Converts time in milliseconds to time in minutes."""

    return milliseconds / 60000


def convert_time_str(minutes: float) -> str:

    """Converts a time given in minutes to hours, minutes and seconds in a string."""

    if minutes % 60 != minutes:
        hours = minutes // 60
        minutes -= hours * 60
    else:
        hours = 0

    seconds = (minutes * 60) % 60
    minutes -= seconds / 60

    return f"{int(hours):03d}:{int(minutes):02d}:{int(seconds):02d}"


def get_date_range(date_range: tuple[str, str] | str) -> list:

    """Creates the date range from the upper and lower date values."""

    start_date = datetime.strptime(date_range[0], DATE_FORMAT)
    end_date = datetime.strptime(date_range[1], DATE_FORMAT)
    change_in_days = end_date - start_date

    return [datetime.strftime(start_date + timedelta(days=_), DATE_FORMAT) for _ in range(change_in_days.days + 1)]


# Analyzing data
def get_x_vals(stats: dict, x_type: str, date_range: list[tuple]) -> list:

    """Gets the specified x value within a given date range."""

    if x_type in X_OPTIONS.values() and x_type != X_OPTIONS[1]:
        return [round(stats[date][x_type]) for date in date_range]
    else:  # Date
        return date_range


def get_y_vals(stats: dict, y_type: str, date_range: list[tuple]) -> list:

    """Returns a list of the specified y values within the given date range."""

    return [stats[date][y_type] for date in date_range]


def zip_values(x_vals: list, y_vals: list) -> list:

    """Returns a list of the specified X and Y values packaged together in tuples, with X at index 0 of the tuple."""

    return [(x_vals[_], y_vals[_]) for _ in range(len(x_vals))]


def sort_values(values: list[tuple]) -> list[tuple]:

    """Returns a list of tuples sorted by x value (the value at index 0 of the inner tuple."""

    return sorted(values, key=operator.itemgetter(0))  # Sorts by first index of inner tuple


def get_vals(stats: dict, x_type: str, y_type: str, date_range="all") -> list[tuple]:

    """
    Returns a list of tuples with the specified x values first and specified y values second. Values are within the
    specified date range.
    """

    # Getting date range
    if date_range == "all":
        lower = list(stats.keys())[0]  # First date recorded
        upper = list(stats.keys())[-1]  # Last date recorded
        date_list = get_date_range((lower, upper))  # List of all dates
    else:
        date_list = get_date_range(date_range)  # List of dates in the specified range

    x_vals = get_x_vals(stats, x_type, date_list)  # X
    y_vals = get_y_vals(stats, y_type, date_list)  # Y

    values = zip_values(x_vals, y_vals)  # One list of (x, y)

    # Sort values by x
    values = sort_values(values)

    return values
