# Main interface
__author__ = "Matteo Golin"

# Imports
from typeTracker.tools.load import read_json, get_stats
from typeTracker.tools.display import console_display_all_time, graph_data
from typeTracker.tools.modify import get_vals
from typeTracker.inputs import get_user_choice

# Loading in data
dataset = read_json()
stats, all_time_stats = get_stats(dataset)

# Main loop to continue
quit_program = ""
while quit_program.lower() != "q":

    # Console stat display
    console_display_all_time(all_time_stats)

    # Graphing display
    x_head, y_head = get_user_choice()
    values = get_vals(stats, x_head, y_head)
    graph_data(values, (x_head, y_head))

    # Prompt for continue
    quit_program = input("Press enter to continue, Q to quit: ")
