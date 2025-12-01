from datetime import date

class FitnessLog:
    def __init__(self, user_id, log_date: date, steps, distance, calories):
        self.user_id = user_id
        self.log_date = log_date
        self.steps = steps
        self.distance = distance
        self.calories = calories