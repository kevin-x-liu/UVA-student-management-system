"""project_a_10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # logs user out and redirects to login page
    path('logout/', LogoutView.as_view(), name='logout'),
    path('addcourse/', views.AddCourse.as_view(), name='addCourse'),
    path('addcoursedb/', views.addCourseDB, name='addCourseDB'),
    path('addassignment/', views.AddAssignment, name='addAssignment'),
    path('addassignmentdb/', views.addAssignmentDB, name='addAssignmentDB'),
    path('course_registry/<str:course_name>', views.displayStudentRegistry, name='students'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/upload/', views.upload_note, name='upload_note'),
    path('calendar/<int:year>/<str:month>/', views.calendar_func, name='calendar'),
    path('calendar/', views.calendar_func2, name='calendar2'),
    path('deleteCourse/<int:course_id>', views.deleteCourse, name='deleteCourse'),
    path('deleteAssignment/<int:assignment_id>', views.deleteAssignment, name='deleteAssignment'),

    path('assignments/', views.assignment_list, name="assignment_list"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
