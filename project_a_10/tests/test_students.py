from django.test import TestCase

from django.contrib.auth.models import User
from ..models import Course
from ..models import Assignment
import django.contrib.auth


class TestStudentLists(TestCase):

    def test_check_if_course_has_the_right_3_people(self):

        user1_1 = User.objects.create_user('arjen')
        user1_1.first_name = 'arjen'
        user1_1.last_name = 'robben'
        user1_1.save()

        c1_1 = Course(course_num='ATT1000', course_name='AttendanceTest1', username=user1_1)
        c1_1.save()

        user1_2 = User.objects.create_user('frank')
        user1_2.first_name = 'frank'
        user1_2.last_name = 'ribery'
        user1_2.save()

        c1_2 = Course(course_num='ATT1000', course_name='AttendanceTest1', username=user1_2)
        c1_2.save()

        user1_3 = User.objects.create_user('robert')
        user1_3.first_name = 'robert'
        user1_3.last_name = 'lewandowski'
        user1_3.save()

        c1_3 = Course(course_num='ATT1000', course_name='AttendanceTest1', username=user1_3)
        c1_3.save()

        user1_4 = User.objects.create_user('david')
        user1_4.first_name = 'david'
        user1_4.last_name = 'alaba'
        user1_4.save()

        c1_4 = Course(course_num='ATT1001', course_name='AAttendanceTest1', username=user1_3)
        c1_4.save()

        attendanceList = Course.objects.filter(course_num = 'ATT1000')
        userlist = []

        for i in range(len(attendanceList)):
            userlist.append(attendanceList[i].username.username)
        assert len(attendanceList) == 3 and 'arjen' in userlist and 'frank' in userlist and 'robert' in userlist

    def test_check_that_no_people_in_this_course(self):

        user2_1 = User.objects.create_user('edison')
        user2_1.first_name = 'edison'
        user2_1.last_name = 'cavani'
        user2_1.save()

        c2_1 = Course(course_num='ATT2000', course_name='ATT2001', username=user2_1)
        c2_1.save()

        user2_2 = User.objects.create_user('luis')
        user2_2.first_name = 'luis'
        user2_2.last_name = 'suarez'
        user2_2.save()

        c2_2 = Course(course_num='ATT20001A', course_name='ATT', username=user2_2)
        c2_2.save()

        emptyAttendance = Course.objects.filter(course_num = 'ATT2001')

        assert len(emptyAttendance) == 0