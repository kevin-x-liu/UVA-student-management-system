from django.contrib import admin

from .models import Course, Assignment, Note

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Note)