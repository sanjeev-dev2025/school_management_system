from django.contrib import admin

# Register your models here.
from assignments.models import Assignment,AssignmentSubmission
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)