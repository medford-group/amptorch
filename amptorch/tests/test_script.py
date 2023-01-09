"""
Test script to be executed before pushing or submitting a PR to master
repository.
"""

import unittest

from .training_test_gmp import test_training_gmp


class TestMethods(unittest.TestCase):
    def test_training_scenarios_gmp(self):
        test_training_gmp()


if __name__ == "__main__":
    unittest.main(warnings="ignore")
