from django.test import TestCase

from django.contrib.auth.models import User
from ..models import Course
import django.contrib.auth


class TestCourses(TestCase):

    def test_check_if_kevin_has_course(self):
        user1 = User.objects.create_user('kevin')
        user1.first_name = 'kevin'
        user1.last_name = 'kern'
        user1.save()

        c1_1 = Course(course_num='TEST1000', course_name='TestingCourse0', username=user1)
        c1_1.save()

        # # print(User.objects.all())
        courseTestKevin = Course.objects.filter(course_num='TEST1000', username=user1)[0]
        assert courseTestKevin.username.username == 'kevin'
        # assert userKevin.username == 'kevin'

    def test_check_that_asia_does_not_have_courses(self):
        user2 = User.objects.create_user('asia')
        user2.first_name = 'asia'
        user2.last_name = 'halter'
        user2.save()

        emptyListAsia = Course.objects.filter(username = user2)
        assert len(emptyListAsia) == 0

    def test_check_if_josephine_has_5_courses(self):
        user3 = User.objects.create_user('josephine')
        user3.first_name = 'josephine'
        user3.last_name = 'johannes'
        user3.save()

        c3_1 = Course(course_num='TEST1001', course_name='TestingCourse1', username=user3)
        c3_1.save()

        c3_2 = Course(course_num='TEST1002', course_name='TestingCourse2', username=user3)
        c3_2.save()

        c3_3 = Course(course_num='TEST1003', course_name='TestingCourse3', username=user3)
        c3_3.save()

        c3_4 = Course(course_num='TEST1004', course_name='TestingCourse4', username=user3)
        c3_4.save()

        c3_5 = Course(course_num='TEST1005', course_name='TestingCourse5', username=user3)
        c3_5.save()

        courseListJosephine = Course.objects.filter(username = user3)
        assert len(courseListJosephine) == 5

    def test_check_if_course_has_3_people(self):
        user4_1 = User.objects.create_user('adam')
        user4_1.first_name = 'adam'
        user4_1.last_name = 'sandler'
        user4_1.save()

        c4_1 = Course(course_num='TEST4000', course_name='TestingCourse4000', username=user4_1)
        c4_1.save()

        user4_2 = User.objects.create_user('bob')
        user4_2.first_name = 'bob'
        user4_2.last_name = 'sponge'
        user4_2.save()

        c4_2 = Course(course_num='TEST4000', course_name='TestingCourse4000', username=user4_2)
        c4_2.save()

        user4_3 = User.objects.create_user('connor')
        user4_3.first_name = 'connor'
        user4_3.last_name = 'mcgregor'
        user4_3.save()

        c4_3 = Course(course_num='TEST4000', course_name='TestingCourse4000', username=user4_3)
        c4_3.save()

        courseList4000 = Course.objects.filter(course_num = 'TEST4000')
        assert len(courseList4000) == 3