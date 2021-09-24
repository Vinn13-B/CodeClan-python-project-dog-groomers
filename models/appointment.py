# create Appointment class with required objects and methods
# for MVP, 'time' object will only offer 0800, 1000, 1200, 1400, 1600

class Appointment:

    def __init__(self, time, dog, id = None):
        self.time = time
        self.dog = dog
        self.id = id

    def check_time(time):
        acceptable_times = ["0800", "1000", "1200", "1400", "1600"]
        if time in acceptable_times:
            pass
        else:
            return "This time is unavailable"
