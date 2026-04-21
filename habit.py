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
    parser.add_argument("--habit")
    parser.add_argument("--session")
    args = parser.parse_args()

    if args.habit_create:
        tracker.habit_create(args.habit_create)
    
    if args.habit and args.session:
        tracker.track_session(args.habit, args.session)

    storage.save(data)

    print(tracker.data)

if __name__ == "__main__":
    main()