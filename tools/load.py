# Functions for loading data

__author__ = "Matteo Golin"

# Imports
import json
from typeTracker.tools.constants import DATASET_LABELS, LESSON_LABELS, ALL_TIME_LABELS
from typeTracker.tools.modify import convert_time_minutes

# CONSTANTS
FILENAME = "./resources/typing-data.json"


# Reading function
def read_json() -> dict:

    # Empty dictionary to store data
    dataset = {}

    with open(FILENAME, 'r') as file:

        data = json.load(file)  # Load data

        lesson_num = 0  # Var to track how many lessons

        # Iterating through lesson data
        for lesson in data:

            # Stripping data
            date, timestamp = lesson["timeStamp"].split("T")
            timestamp = timestamp.replace(".000Z", "")
            speed = lesson["speed"]
            errors = lesson["errors"]
            time = lesson["time"]
            lesson_num += 1

            # Lesson data
            lesson_data = {
                DATASET_LABELS[0]: timestamp,
                DATASET_LABELS[4]: lesson_num,
                DATASET_LABELS[5]: speed / 5,
                DATASET_LABELS[2]: errors,
                DATASET_LABELS[3]: time
            }

            # Create the entry in the new dictionary
            if dataset.get(date) is not None:  # Entry exists for this date
                dataset[date].append(lesson_data)
            else:  # Entry doesn't exist for this date
                dataset[date] = [lesson_data]

    return dataset


# Packaging into stats
def get_stats(dataset: dict) -> tuple:

    average_stats = {}

    # All time stats
    overall_wpm_total = 0
    all_time_wpm = 0
    all_time_error = 0
    all_time_practice_time = 0
    total_lessons = 0

    for date in dataset:

        # Lesson stats
        lessons = len(dataset[date])
        wpm_sum = 0
        error_sum = 0
        total_time = 0

        # Track highest wpm and how many errors it had
        highest_wpm = 0
        highest_wpm_errors = 0

        total_lessons += lessons  # Total lessons

        for lesson in dataset[date]:

            wpm_sum += lesson[DATASET_LABELS[5]]
            error_sum += lesson[DATASET_LABELS[2]]
            total_time += lesson[DATASET_LABELS[3]]

            # Highest wpm that day
            if lesson[DATASET_LABELS[5]] > highest_wpm:
                highest_wpm = lesson[DATASET_LABELS[5]]
                highest_wpm_errors = lesson[DATASET_LABELS[2]]

        overall_wpm_total += wpm_sum  # Total wpm for average calculation
        all_time_error += error_sum  # All time average error
        all_time_practice_time += total_time  # All time practice time

        # Highest wpm
        if highest_wpm > all_time_wpm:
            all_time_wpm = highest_wpm

        # Lesson stat dict
        lesson_stats = {
            LESSON_LABELS[0]: round(wpm_sum / lessons, 2),
            LESSON_LABELS[1]: round(error_sum / lessons, 2),
            LESSON_LABELS[2]: highest_wpm,
            LESSON_LABELS[3]: highest_wpm_errors,
            LESSON_LABELS[4]: convert_time_minutes(total_time),
            LESSON_LABELS[5]: lessons
        }

        average_stats[date] = lesson_stats

    # Calculating all time stats
    all_time_stats = {
        ALL_TIME_LABELS[0]: all_time_wpm,
        ALL_TIME_LABELS[1]: round(all_time_error / total_lessons, 2),
        ALL_TIME_LABELS[2]: convert_time_minutes(all_time_practice_time),
        ALL_TIME_LABELS[3]: total_lessons,
        ALL_TIME_LABELS[4]: round(overall_wpm_total / total_lessons, 2)
    }

    return average_stats, all_time_stats
