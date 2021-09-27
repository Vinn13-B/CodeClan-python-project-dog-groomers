# creating run_tests for Dog,Appointment, Groomer and Owner classeses

import unittest

from tests.dog_tests import TestDog
from tests.appointment_tests import TestAppointment
from tests.groomer_tests import TestGroomer
from tests.owner_tests import TestOwner
from tests.walk_tests import TestWalk

if __name__ == '__main__':
    unittest.main()