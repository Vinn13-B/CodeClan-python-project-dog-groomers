# setting up Tests for Dog class, testing each required object in class
# will then create class and objects to pass each test

import unittest

from models.dog import Dog

class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog = Dog("Biscuits", "Norfolk Terrier", 8, "Ailie", "None")

    def test_dog_has_name(self):
        self.assertEqual("Biscuits", self.dog.name)

    def test_dog_has_breed(self):
        self.assertEqual("Norfolk Terrier", self.dog.breed)

    def test_dog_has_age(self):
        self.assertEqual(8, self.dog.age)

    def test_dog_has_owner(self):
        self.assertEqual("Ailie", self.dog.owner)

    def test_dog_has_comments(self):
        self.assertEqual("None", self.dog.comments)
    
