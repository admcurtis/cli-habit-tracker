#%%
import unittest
from habittracker import HabitTracker

#%%

class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        self.test_input = {
            'habits': {
                'machinelearn': {
                    'id': 1,
                    'created': '2026-04-21'
                }
            },
            'sessions': {},
            'progress': {}
        }

    def test_create_habit(self):
        tracker = HabitTracker(self.test_input)
        tracker.habit_create("maths")
        self.assertIn("maths", tracker.data["habits"])

    def test_create_habit_exists(self):
        tracker = HabitTracker(self.test_input)
        tracker.habit_create("machinelearn")
        self.assertEqual(len(tracker.data["habits"]), 1)
        self.assertIn("machinelearn", tracker.data["habits"])

if __name__ == "__main__":
    unittest.main()