from ESPractica.P3_mock_demo.src import User as u
import os
import sys
import unittest
import pickle

class TestUser(unittest.TestCase):
    def test_init_X(self):
        for ix, input in enumerate(self.test_cases['input']):
            us = u.User(input, self.test_cases['K'][ix])
            self.testing.assert_array_equal(u.X, self.test_cases['shape'][ix])