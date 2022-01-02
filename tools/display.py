# Functions for displaying data
__author__ = "Matteo Golin"

# Imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as mplstyle
from tools.modify import convert_time_str
from tools.constants import LESSON_LABELS, ALL_TIME_LABELS, X_OPTIONS

# Constants
STYLE_FILE = "./resources/wpm.mplstyle"


# Style plot
mplstyle.use(STYLE_FILE)


# Curve fitting
def fit_curve(x: list, y: list, deg: int) -> tuple[np.ndarray, np.ndarray]:

    """Returns the x and y points generate by a curve that fits the given x and y values."""

    point_interval = 30 * len(x)

    if type(x[0]) == str:
        new_x = [_ for _ in range(len(x))]
        curve_x = np.linspace(new_x[0], new_x[-1], point_interval)
        curve = np.polyfit(new_x, y, deg)
    else:
        curve_x = np.linspace(x[0], x[-1], point_interval)  # Points generated for the curve to follow
        curve = np.polyfit(x, y, deg)  # Curve equation

    curve_y = np.polyval(curve, curve_x)  # Y points

    return curve_x, curve_y


# Graphing
def graph_data(values: list[tuple], headers: tuple[str, str], deg: int):

    """
    Takes a list of tuples containing X and Y points in format (x, y), and plots them. Labels axes using
    provided headers.
    """

    # Getting units
    UNITS = {
        LESSON_LABELS[5]: " (minutes)",
        "Date": " (days)"
    }

    # Unpacking values
    x_points, y_points = [], []
    for value in values:
        x, y = value

        # Remove year from date stamp to prevent squishing
        if headers[0] == X_OPTIONS[1] and len(values) > 10:
            x_points.append(x[-5:])
        else:
            x_points.append(x)

        y_points.append(y)

    x_head, y_head = headers  # Axis labels
    if UNITS.get(x_head) is not None:
        x_head += UNITS.get(x_head)
    if UNITS.get(y_head) is not None:
        y_head += UNITS.get(y_head)

    curve_x, curve_y = fit_curve(x_points, y_points, deg)  # Get curve

    # Setting new icon
    plt.figure("Type Tracker")  # Window label
    manager = plt.get_current_fig_manager()
    manager.window.wm_iconbitmap("resources/typetrackercap_icon.ico")

    plt.plot(x_points, y_points, 'o', curve_x, curve_y, '-')  # Plot data points and curve

    # Label graph
    plt.xlabel(x_head)
    plt.ylabel(y_head)
    plt.title(f"{x_head} vs {y_head}")

    plt.show()  # Display


# Console display functions
def console_display_stats(stats: dict, stat_name: str) -> None:

    print(f"Date{' ' * 7}| {stat_name}")

    for date in stats:

        if LESSON_LABELS[4] == stat_name:
            print(f"{date} | {convert_time_str(stats[date][stat_name])}")
        else:
            print(f"{date} | {stats[date][stat_name]}")


def console_display_all_time(all_time_stats: dict) -> None:

    print(f"{'=' * 10}All Time Statistics{'=' * 10}")

    for label in all_time_stats:

        if ALL_TIME_LABELS[2] == label:
            print(f"{label}: {convert_time_str(all_time_stats[label])}")
        else:
            print(f"{label}: {all_time_stats[label]}")

    print()


def console_display_choices(choices: dict, x_or_y: str):

    """Prints the choices for X and Y headers to the console."""

    print(f"Enter the number associated with the {x_or_y} value you want plotted.")

    for index in choices:
        print(f"{index} - {choices[index]}")
    print()
