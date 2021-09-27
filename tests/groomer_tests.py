# setting up Tests for Groomer class, testing each required object in class
# will then create class and objects to pass each test

import unittest

from models.groomer import Groomer

class TestGroomer(unittest.TestCase):

    def setUp(self):
        self.groomer = Groomer("Ailie", "07930444444")

    def test_groomer_has_name(self):
        self.assertEqual("Ailie", self.groomer.name)

    def test_groomer_has_contact_number(self):
        self.assertEqual("07930444444", self.groomer.contact_number)