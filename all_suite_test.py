import unittest

from unittest.loader import makeSuite

from test_cases.logout import TestLogout
from test_cases.add_a_new_player import TestAddANewPlayer
from test_cases.redirect_to_players import TestRedirection
from test_cases.homepage_language_change import TestHomepageLanguageChange
from test_cases.login_language_change import TestLoginLanguageChange
from test_cases.login_to_the_system import TestLoginPage
from test_cases.framework_test import Test


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLogout))
    test_suite.addTest(makeSuite(TestAddANewPlayer))
    test_suite.addTest(makeSuite(TestRedirection))
    test_suite.addTest(makeSuite(TestHomepageLanguageChange))
    test_suite.addTest(makeSuite(TestLoginLanguageChange))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())