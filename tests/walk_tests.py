# setting up Tests for Walk class, testing each required object in class
# tests will also need to be created for required methods
# will then create class, objects and methods to pass each test

import unittest

from models.walk import Walk

class TestWalk(unittest.TestCase):

    def setUp(self):
        self.walk = Walk("30/09/2021", "0900", 5, "Elvis")
    
    def test_walk_has_date(self):
        self.assertEqual("30/09/2021", self.walk.date)

    def test_walk_has_time(self):
        self.assertEqual("0900", self.walk.time)

    def test_walk_has_capacity(self):
        self.assertEqual(5, self.walk.capacity)

    def test_walk_has_dog(self):
        self.assertEqual("Elvis", self.walk.dog)

    def test_walk_can_increase_head_count(self):
        Walk.increase_head_count(self.walk)
        self.assertEqual(1, self.walk.head_count)

    def test_walk_can_decrease_head_count(self):
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.decrease_head_count(self.walk)
        self.assertEqual(1, self.walk.head_count)

    def test_check_headcount_pass(self):
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        self.assertEqual(None, Walk.increase_head_count(self.walk))

    def test_check_headcount_fail(self):
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        Walk.increase_head_count(self.walk)
        self.assertEqual("This walk is now full", Walk.increase_head_count(self.walk))