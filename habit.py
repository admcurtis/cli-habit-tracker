import argparse
import json
from habittracker import HabitTracker
from storage import JSONStorage


def main():

    storage = JSONStorage()
    data = storage.load()

    tracker = HabitTracker(data)

    parser = argparse.ArgumentParser()
    parser.add_argument("--habit_create")
    args = parser.parse_args()

    if args.habit_create:
        tracker.habit_create(args.habit_create)

    print(tracker.data)

if __name__ == "__main__":
    main()