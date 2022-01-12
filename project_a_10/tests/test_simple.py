from django.test import SimpleTestCase


class TestFirst(SimpleTestCase):

    def test_is_very_simple(self):
        assert 1 == 1

    def test_is_just_as_simple(self):
        assert 3 == 3

