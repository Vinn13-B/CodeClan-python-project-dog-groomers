# create Day class with required object and methods
# for MVP, 'time' object will only offer 0800, 1000, 1200, 1400, 1600

class Day:

    def __init__(self):
        self.appointments = []

    def add_appointment(self, new_appointment):
        self.appointments.append(new_appointment)

    def check_availability(self, time):
        for self.appointment in self.appointments:
            if self.appointment.time == time:
                return "This time is not available"
            else:
                pass