from datetime import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from bs4 import BeautifulSoup
from lxml import html

from django.contrib.auth.decorators import login_required
from .models import Course, Note
from .models import Assignment

from .forms import NoteForm
import requests

from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# below tag will block unsignin users from accesses the homepage
@login_required(login_url='/login')
def index(request):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    course_list = Course.objects.filter(
            username=request.user
        )
    
    print(course_list)
    assignment_list = Assignment.objects.filter(
            username=request.user
        )
    context = {'course_list': course_list,
               'assignment_list': assignment_list,
               "current_year": current_year,
                "current_month": current_month,}

    return render(request, 'index.html', context)


# brings user to login page
def login(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]
    context = {"current_year": current_year,
                "current_month": current_month,}

    return render(request, 'login.html', context)


class AddCourse(generic.ListView):
    model = Course
    template_name = 'add-course.html'


def addCourseDB(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]
    context = {"current_year": current_year,
                "current_month": current_month,}

    current_user = request.user

    c = Course(course_num=request.POST['course_num'], course_name=request.POST['course_name'], username=current_user)
    c.save()
    return HttpResponseRedirect(reverse('index', args=()))


def AddAssignment(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    model = Assignment

    course_list = Course.objects.filter(
        username=request.user
    )
    print(course_list)
    context = {'course_list': course_list,
                "current_year": current_year,
                "current_month": current_month,}
    return render(request, 'add-assignment.html', context)


def addAssignmentDB(request):
    print(request.POST['course_id'])
    course = Course.objects.filter(
        id=request.POST['course_id']
    )[0]
    current_user = request.user
    date = request.POST['duetime'].split('-')
    dayTime = date[2].split('T')
    day = dayTime[0]
    hour = dayTime[1].split(':')[0]
    minute = dayTime[1].split(':')[1]

    a = Assignment(assignment_name=request.POST['assignment_name'], assignment_due_date=datetime(int(date[0]), int(date[1]), int(day), int(hour), int(minute), 59, 342380), course_num=course, username=current_user)
    a.save()
    return HttpResponseRedirect(reverse('index', args=()))


def displayStudentRegistry(request, course_name):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    r = requests.get('https://louslist.org/sectiontip.php?Semester=1218&ClassNumber='+course_name)
    course_description = 'Description not available'
    course_info = 'Course information not available'
    if r.status_code == 200:
        # return HttpResponse(r.text)
        parsed_html = BeautifulSoup(r.text, features="lxml")
        course_description = parsed_html.find("td", {"class": "InfoSISDescription"}).text
        course_info = parsed_html.findAll("td", {"class": "InfoClass"})[1].text
        course_instructor = parsed_html.findAll("td", {"class": "InfoMeetings"})[1].find('table').findAll('td')[0].text
        course_time = parsed_html.findAll("td", {"class": "InfoMeetings"})[1].find('table').findAll('td')[1].text
        course_room = parsed_html.findAll("td", {"class": "InfoMeetings"})[1].find('table').findAll('td')[2].text

    r.close()

    student_list = Course.objects.filter(course_num=course_name)
    return render(request, 'student_reg.html',
                  {'student_list': student_list,
                   'description': course_description,
                   'course': course_info,
                   'course_instructor': course_instructor,
                   'course_time':  course_time,
                   'course_room': course_room,
                   "current_year": current_year,
                    "current_month": current_month,})


def note_list(request):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    notes = Note.objects.filter(
        username=request.user
    )

    return render(request, 'note_list.html', {
        'notes': notes,
        "current_year": current_year,
        "current_month": current_month,
    })


def upload_note(request):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    course_list = Course.objects.filter(
        username=request.user
    )

    if request.method == 'POST':
        course = Course.objects.filter(
            id=request.POST['course_num']
        )[0]
        print(request.POST['course_num'])
        form = NoteForm(request.POST, request.FILES, instance=Note(username=request.user, course_num=course))
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {
        'form': form,
        'course_list': course_list,
        "current_year": current_year,
        "current_month": current_month,
    })


def deleteCourse(request, course_id):
    courseDelete = Course.objects.get(id= course_id)
    courseDelete.delete()
    return HttpResponseRedirect(reverse('index', args=()))


def deleteAssignment(request, assignment_id):
    assignmentDelete = Assignment.objects.get(id=assignment_id)
    assignmentDelete.delete()
    return HttpResponseRedirect(reverse('index', args=()))

#############################
#
# The folowing resources were used to understand the basics of building a calendar in html
#
# REFERENCES
#
# Title: How To Add A Calendar To Your Website - Django Wednesdays #2
# Author: Codemy.com
# Date: 01/27/2021
# Code version: (At time of video)
# URL: https://www.youtube.com/watch?v=4EJlrweJE-M
# Software License: N/A
# (No access to source code)
#
# Title: Event Calendar with Django and Python
# Author: Sajib Hossain
# Date: 07/29/2020
# Code version: (Latest)
# URL: https://www.youtube.com/watch?v=dy1oG_XqsgY
# Source Code: https://github.com/sajib1066/event-calendar
# Software License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/> Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
#
#############################

def calendar_func(request, year, month):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    name = request.user
    month_non_cap = month
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    if "29" not in cal:
        days_cur_month = 28
    elif "30" not in cal:
        days_cur_month = 29
    elif "31" not in cal:
        days_cur_month = 30
    else:
        days_cur_month = 31

    assignmentList = Assignment.objects.filter(username = request.user)

    eventlist = []
    daycount = []
    daycountstr = []
    days_order = []
    for k_day in range(days_cur_month+1):
        eventlist.append("")
        daycount.append(3)
        daycountstr.append("")
        days_order.append(days_cur_month-k_day)

    for each in assignmentList:
        # print(each.assignment_due_date.year)
        # print(each.assignment_due_date.month)
        # print(current_year)
        # print(month_number)
        if each.assignment_due_date.year == year and each.assignment_due_date.month == month_number:
            # print("yes")
            # print(each.assignment_due_date.day)
            eventlist[each.assignment_due_date.day] = eventlist[each.assignment_due_date.day] + '<li style="background-color:#9AE3E6;">' + each.assignment_name + '</li>' + "<br style='line-height: 4px;'/>"
            daycount[each.assignment_due_date.day] = daycount[each.assignment_due_date.day] - 1
    
    for k_day in range(days_cur_month+1):
        if daycount[k_day] > 0:
            for i in range(daycount[k_day]):
                daycountstr[k_day] = daycountstr[k_day] + "<br/>"

    # print(eventlist)

    #for j_day in range(days_cur_month+1):
    #    eventlist.append("hi" + str(j_day))

    for i_day in days_order:
        if i_day != 0:
            cal = cal.replace('>' + str(i_day) + '<', ' valign="top" style="font-family:helvetica;" ' + '>' + str(i_day) + '<br/>'+ eventlist[i_day] + daycountstr[i_day] + '<', 1)

    # cal = cal.replace('<tr><th> cl', '<tr style="font-family:helvetica;"><th> cl', 1)
    cal = cal.replace('<tr>', '<tr style="font-family:helvetica;">', 1)
    # weekdays_replace = ['>Mon<', '>Tue<', '>Wed<', '>Thu<', '>Fri<', '>Sat<', '>Sun<']
    # for rep in weekdays_replace:
    #     cal = cal.replace(rep, '><p style="font-family:helvetica;">' + rep[1:4] + '</p><', 1)

    # cal = cal.replace('>' + "1" + '<', '>' + "blablablab labla blablalblablablalblabalbalablalbalablablab" + '<')
    cal = cal.replace('table border="0"', 'table style="width: 90%;table-layout:fixed; word-wrap: break-word; align="left"; valign="top"; border=1px solid #ddd!important" border="1"', 1)
    cal = cal.replace('cellpadding="0"', 'cellpadding="10"', 1)
    # cal = cal.replace('<tr>', '<tr style="border=1">', 1)
    # cal = cal.replace('<td>', '<td style="border-left: none">')

    cal = cal.replace('class="month"', 'class="table table-bordered"', 1)

    next_list = {"january": "february", "february": "march", "march": "april", "april": "may", "may": "june", "june": "july",
                "july": "august", "august": "september", "september": "october", "october": "november",
                "november": "december", "december": "january"}

    prev_list = {"january": "december", "february": "january", "march": "february", "april": "march", "may": "april", "june": "may",
                "july": "june", "august": "july", "september": "august", "october": "september",
                "november": "october", "december": "november"}

    if month_non_cap == "december":
        n_m_year = int(year) + 1
    else:
        n_m_year = int(year)
    if month_non_cap == "january":
        p_m_year = int(year) - 1
    else:
        p_m_year = int(year)

    return render(request,
            'calendar.html', {
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "current_month": current_month,
            "next_month": next_list[month_non_cap],
            "n_m_year": str(n_m_year),
            "prev_month": prev_list[month_non_cap],
            "p_m_year": str(p_m_year),
           })

def calendar_func2(request):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]
    month = current_month
    year = current_year

    name = request.user
    month_non_cap = month
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    if "29" not in cal:
        days_cur_month = 28
    elif "30" not in cal:
        days_cur_month = 29
    elif "31" not in cal:
        days_cur_month = 30
    else:
        days_cur_month = 31

    assignmentList = Assignment.objects.filter(username = request.user)

    eventlist = []
    daycount = []
    daycountstr = []
    days_order = []
    for k_day in range(days_cur_month+1):
        eventlist.append("")
        daycount.append(3)
        daycountstr.append("")
        days_order.append(days_cur_month-k_day)

    for each in assignmentList:
        # print(each.assignment_due_date.year)
        # print(each.assignment_due_date.month)
        # print(current_year)
        # print(month_number)
        if each.assignment_due_date.year == year and each.assignment_due_date.month == month_number:
            # print("yes")
            # print(each.assignment_due_date.day)
            eventlist[each.assignment_due_date.day] = eventlist[each.assignment_due_date.day] + '<li style="background-color:#9AE3E6;">' + each.assignment_name + '</li>' + "<br style='line-height: 4px;'/>"
            daycount[each.assignment_due_date.day] = daycount[each.assignment_due_date.day] - 1
    
    for k_day in range(days_cur_month+1):
        if daycount[k_day] > 0:
            for i in range(daycount[k_day]):
                daycountstr[k_day] = daycountstr[k_day] + "<br/>"

    # print(eventlist)

    #for j_day in range(days_cur_month+1):
    #    eventlist.append("hi" + str(j_day))

    for i_day in days_order:
        if i_day != 0:
            cal = cal.replace('>' + str(i_day) + '<', ' valign="top" style="font-family:helvetica;" ' + '>' + str(i_day) + '<br/>'+ eventlist[i_day] + daycountstr[i_day] + '<', 1)

    # cal = cal.replace('<tr><th> cl', '<tr style="font-family:helvetica;"><th> cl', 1)
    cal = cal.replace('<tr>', '<tr style="font-family:helvetica;">', 1)
    # weekdays_replace = ['>Mon<', '>Tue<', '>Wed<', '>Thu<', '>Fri<', '>Sat<', '>Sun<']
    # for rep in weekdays_replace:
    #     cal = cal.replace(rep, '><p style="font-family:helvetica;">' + rep[1:4] + '</p><', 1)

    # cal = cal.replace('>' + "1" + '<', '>' + "blablablab labla blablalblablablalblabalbalablalbalablablab" + '<')
    cal = cal.replace('table border="0"', 'table style="width: 90%;table-layout:fixed; word-wrap: break-word; align="left"; valign="top"; border=1px solid #ddd!important" border="1"', 1)
    cal = cal.replace('cellpadding="0"', 'cellpadding="10"', 1)
    # cal = cal.replace('<tr>', '<tr style="border=1">', 1)
    # cal = cal.replace('<td>', '<td style="border-left: none">')

    cal = cal.replace('class="month"', 'class="table table-bordered"', 1)

    next_list = {"january": "february", "february": "march", "march": "april", "april": "may", "may": "june", "june": "july",
                "july": "august", "august": "september", "september": "october", "october": "november",
                "november": "december", "december": "january"}

    prev_list = {"january": "december", "february": "january", "march": "february", "april": "march", "may": "april", "june": "may",
                "july": "june", "august": "july", "september": "august", "october": "september",
                "november": "october", "december": "november"}

    if month_non_cap == "december":
        n_m_year = int(year) + 1
    else:
        n_m_year = int(year)
    if month_non_cap == "january":
        p_m_year = int(year) - 1
    else:
        p_m_year = int(year)

    return render(request,
            'calendar.html', {
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "current_month": current_month,
            "next_month": next_list[month_non_cap],
            "n_m_year": str(n_m_year),
            "prev_month": prev_list[month_non_cap],
            "p_m_year": str(p_m_year),
           })

def assignment_list(request):

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    monthlist = [" ", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    current_month = monthlist[current_month]

    assignments = Assignment.objects.filter(
        username=request.user
    )

    return render(request, 'assignment_list.html', {
        'assignments': assignments,
        "current_year": current_year,
        "current_month": current_month,
    })