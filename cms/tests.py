from unittest import expectedFailure

from django.test import TestCase


class NullTest(TestCase):
    def test_success(self):
        self.assertEqual(1, 1)

    @expectedFailure
    def test_fail(self):
        self.assertEqual(1, 2)
