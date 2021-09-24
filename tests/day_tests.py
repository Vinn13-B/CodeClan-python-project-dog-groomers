# setting up Tests for Day class, testing each required object in class
# tests will also need to be created for required methods
# will then create class, objects and methods to pass each test
# for MVP, 'time' object will only offer 0800, 1000, 1200, 1400, 1600

import unittest

from models.day import Day
from models.appointment import Appointment

class TestDay(unittest.TestCase):

    def setUp(self):
        self.appointment1_pass = Appointment("0800", "Biscuits")
        self.appointment2_pass = Appointment("1000", "Elvis")
        self.appointment3_fail = Appointment("0800", "Daisy")
        self.day = Day()

    def test_can_add_appointemnt_to_day(self):
        self.day.add_appointment(self.appointment1_pass)
        self.assertEqual(1, len(self.day.appointments))

    def test_check_availability_pass(self):
        self.day.add_appointment(self.appointment1_pass)
        self.assertEqual(None, Day.check_availability(self.day, self.appointment2_pass.time))

    def test_check_availability_fail(self):
        self.day.add_appointment(self.appointment1_pass)
        self.assertEqual("This time is not available", Day.check_availability(self.day, self.appointment3_fail.time))

