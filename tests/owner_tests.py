# setting up Tests for Onwer class, testing each required object in class
# will then create class and objects to pass each test

import unittest

from models.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner = Owner("Carol Ann Brown", "07932111111")

    def test_groomer_has_name(self):
        self.assertEqual("Carol Ann Brown", self.owner.name)

    def test_groomer_has_contact_number(self):
        self.assertEqual("07932111111", self.owner.contact_number)