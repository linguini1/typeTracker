# Main interface

__author__ = "Matteo Golin"

# Imports
from typeTracker.tools.load import read_json, get_stats
from typeTracker.tools.display import console_display_stats, console_display_all_time, graph_data
from typeTracker.tools.modify import get_vals

dataset = read_json()
stats, all_time_stats = get_stats(dataset)

console_display_stats(stats, "Highest WPM Error Count")
print()
console_display_all_time(all_time_stats)

headers = ("Date", "Average WPM")
x_head, y_head = headers

values = get_vals(stats, x_head, y_head)
graph_data(values, headers)
