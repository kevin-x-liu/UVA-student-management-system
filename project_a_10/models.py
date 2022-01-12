import datetime
from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User


class Course(models.Model):
    def __str__(self):
        return self.course_num

    course_num = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class Assignment(models.Model):
    def __str__(self):
        return self.assignment_name

    assignment_name = models.CharField(max_length=200)
    assignment_due_date = models.DateTimeField(editable=True)
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class Note(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='notes/pdfs/')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title