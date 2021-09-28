# create Appointment class with required objects and methods
# for MVP, 'time' object will only offer 0800, 1000, 1200, 1400, 1600

class Appointment:

    def __init__(self, date, time, dog, groomer, id = None):
        self.date = date
        self.time = time
        self.dog = dog
        self.groomer = groomer
        self.id = id