import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests import RegisterCoursesTests


# Get all tests from the test clases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)


# Create a test suite combination all test clases
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)