from django.test import TestCase

from django.contrib.auth.models import User
import django.contrib.auth


class TestLogin(TestCase):

    def test_look_for_kevin(self):
        user = User.objects.create_user('kevin')
        user.first_name = 'kevin'
        user.last_name = 'kern'
        user.save()
        # # print(User.objects.all())
        userKevin = User.objects.get(username='kevin')
        assert userKevin.username == 'kevin'
        # assert userKevin.username == 'kevin'
