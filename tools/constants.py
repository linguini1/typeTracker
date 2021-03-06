# Important constants
__author__ = "Matteo Golin"

# Imports
import re

# Constants
DATE_FORMAT = "%Y-%m-%d"  # ISO
ISO_PATTERN = re.compile("^\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$")  # ISO regex pattern yyyy-mm-dd

MAX = 4  # Maximum degree for polynomial interpolation

DATASET_LABELS = [
    "timeStamp",
    "speed",
    "errors",
    "time",
    "lesson",
    "wpm"
]

LESSON_LABELS = [
    "Average WPM",
    "Average Error",
    "Highest WPM",
    "Highest WPM Error Count",
    "Practice Time",
    "Lessons"
]

ALL_TIME_LABELS = [
    "Highest WPM",
    "Average Error",
    "Total Practice Time",
    "Total Lessons",
    "Average WPM"
]

X_OPTIONS = {
    1: "Date",
    2: LESSON_LABELS[1],
    3: LESSON_LABELS[4],
    4: LESSON_LABELS[5]
}

Y_OPTIONS = {
    1: LESSON_LABELS[0],
    2: LESSON_LABELS[1],
    3: LESSON_LABELS[2],
    4: LESSON_LABELS[3],
    5: LESSON_LABELS[4],
    6: LESSON_LABELS[5]
}
