from django.test import TestCase

from django.contrib.auth.models import User
from ..models import Course
from ..models import Assignment
import django.contrib.auth
import datetime


class TestAssignments(TestCase):

    def test_check_if_cristiano_has_assignment_for_one_course(self):

        # Adds one class and one assignment for cristiano and checks that cristiano has an assignment with the right name for that class

        user1 = User.objects.create_user('cristiano')
        user1.first_name = 'cristiano'
        user1.last_name = 'ronaldo'
        user1.save()

        c1_1 = Course(course_num='NEW1000', course_name='NewCourse0', username=user1)
        c1_1.save()

        d = datetime.datetime(2021, 12, 12, 23, 55, 59, 342380)
        a1_1 = Assignment(assignment_name = 'HW1', assignment_due_date = d, course_num=c1_1, username=user1)
        a1_1.save()

        assignmentCristiano = Assignment.objects.filter(assignment_name='HW1', username = user1)[0]
        assert assignmentCristiano.assignment_name == 'HW1'

    def test_check_that_leo_has_no_assignments(self):

        # Adds two classes to leo but no assignments, and checks that leo has no assignments

        user2 = User.objects.create_user('leo')
        user2.first_name = 'leo'
        user2.last_name = 'messi'
        user2.save()

        c2_1 = Course(course_num='NEW2001', course_name='NewCourse20', username=user2)
        c2_1.save()

        c2_2 = Course(course_num='NEW2002', course_name='NewCourse21', username=user2)
        c2_2.save()

        d = datetime.datetime(2021, 12, 12, 23, 55, 59, 342380)

        emptyListLeo = Assignment.objects.filter(username = user2)
        assert len(emptyListLeo) == 0

    def test_check_that_there_are_two_different_assignments_with_same_name(self):

        # Adds one class and one assignment to each of two user and checks that two different assignments of same name were created

        user3_1 = User.objects.create_user('Student1')
        user3_1.first_name = 'Student1'
        user3_1.last_name = 'Student'
        user3_1.save()

        c3_1 = Course(course_num='NEW3001', course_name='NewCourse31', username=user3_1)
        c3_1.save()

        d = datetime.datetime(2021, 12, 12, 23, 55, 59, 342380)
        a3_1 = Assignment(assignment_name = 'Project1', assignment_due_date = d, course_num=c3_1, username=user3_1)
        a3_1.save()

        user3_2 = User.objects.create_user('Student2')
        user3_2.first_name = 'Student2'
        user3_2.last_name = 'Student2'
        user3_2.save()

        c3_2 = Course(course_num='NEW3002', course_name='NewCourse32', username=user3_2)
        c3_2.save()

        d = datetime.datetime(2021, 12, 12, 23, 55, 59, 342380)
        a3_2 = Assignment(assignment_name = 'Project1', assignment_due_date = d, course_num=c3_2, username=user3_2)
        a3_2.save()

        assignmentsProject1 = Assignment.objects.filter(assignment_name='Project1')
        assert len(assignmentsProject1) == 2

    def test_check_that_diego_has_the_right_number_of_assignments(self):

        # Add 3 classes and two assignments per class for a user and checks that user has 6 assignments

        user4_1 = User.objects.create_user('diego')
        user4_1.first_name = 'diego'
        user4_1.last_name = 'maradona'
        user4_1.save()

        # Class 1

        c4_1 = Course(course_num='NEW4001', course_name='NewCourse41', username=user4_1)
        c4_1.save()

        d = datetime.datetime(2021, 12, 12, 23, 55, 59, 342380)
        a4_1 = Assignment(assignment_name = 'Course41HW1', assignment_due_date = d, course_num=c4_1, username=user4_1)
        a4_1.save()

        d = datetime.datetime(2021, 12, 12, 23, 50, 50, 342380)
        a4_2 = Assignment(assignment_name = 'Course41HW2', assignment_due_date = d, course_num=c4_1, username=user4_1)
        a4_2.save()

        # Class 2

        c4_2 = Course(course_num='NEW4002', course_name='NewCourse42', username=user4_1)
        c4_2.save()

        d = datetime.datetime(2021, 12, 12, 22, 55, 59, 342380)
        a4_3 = Assignment(assignment_name = 'Course42HW1', assignment_due_date = d, course_num=c4_2, username=user4_1)
        a4_3.save()

        d = datetime.datetime(2021, 12, 12, 22, 50, 50, 342380)
        a4_4 = Assignment(assignment_name = 'Course42HW2', assignment_due_date = d, course_num=c4_2, username=user4_1)
        a4_4.save()

        # Class 3

        c4_3 = Course(course_num='NEW4003', course_name='NewCourse43', username=user4_1)
        c4_3.save()

        d = datetime.datetime(2021, 12, 12, 21, 55, 59, 342380)
        a4_5 = Assignment(assignment_name = 'Course43HW1', assignment_due_date = d, course_num=c4_3, username=user4_1)
        a4_5.save()

        d = datetime.datetime(2021, 12, 12, 21, 50, 50, 342380)
        a4_6 = Assignment(assignment_name = 'Course43HW2', assignment_due_date = d, course_num=c4_3, username=user4_1)
        a4_6.save()

        assignmentsDiego = Assignment.objects.filter(username = user4_1)
        assert len(assignmentsDiego) == 6