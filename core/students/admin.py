from django.contrib import admin

# Register your models here.
from students.models import StudentProfile
admin.site.register(StudentProfile)