# Main interface
__author__ = "Matteo Golin"

# Imports
from tools.load import read_json, get_stats
from tools.display import console_display_all_time, graph_data, console_display_choices
from tools.modify import get_vals
from tools.constants import X_OPTIONS, Y_OPTIONS
from inputs import get_user_choice, parser

# Loading in data
dataset = read_json()
stats, all_time_stats = get_stats(dataset)

# Parsing commandline
arguments = parser.parse_args()


# Display options
if arguments.options:

    console_display_choices(X_OPTIONS, "X")
    console_display_choices(Y_OPTIONS, "Y")

    if not arguments.xy:
        quit()  # Avoids entering console interface


if arguments.xy:  # Command line mode

    x_head, y_head = arguments.xy  # Unpack x and y value indexes
    x_head, y_head = X_OPTIONS[x_head], Y_OPTIONS[y_head]  # Get associated headers

    values = get_vals(stats, x_head, y_head)  # Get values to plot
    graph_data(values, (x_head, y_head), 1)  # Plot values

else:  # Console interface mode
    # Main loop to continue
    quit_program = ""
    while quit_program.lower() != "q":

        # Console stat display
        console_display_all_time(all_time_stats)

        # Graphing display
        x_head, y_head = get_user_choice()  # Get user defined x and y values
        values = get_vals(stats, x_head, y_head)  # Get values to plot
        graph_data(values, (x_head, y_head), 1)  # Plot values

        # Prompt for continue
        quit_program = input("Press enter to continue, Q to quit: ")
