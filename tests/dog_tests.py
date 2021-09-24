# setting up Tests for Dog class, testing each required object in class
# will then create class and objects to pass each test

import unittest

from models.dog import Dog

class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog = Dog("Biscuits", "Norfolk Terrier", 8, "Ailie", "Brown", "07930111111")

    def test_dog_has_name(self):
        self.assertEqual("Biscuits", self.dog.name)

    def test_dog_has_breed(self):
        self.assertEqual("Norfolk Terrier", self.dog.breed)

    def test_dog_has_age(self):
        self.assertEqual(8, self.dog.age)
    
    def test_owner_has_first_name(self):
        self.assertEqual("Ailie", self.dog.owner_first_name)
    
    def test_owner_has_last_name(self):
        self.assertEqual("Brown", self.dog.owner_last_name)
    
    def test_owner_has_contact_number(self):
        self.assertEqual("07930111111", self.dog.owner_contact_number)