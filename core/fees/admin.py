from django.contrib import admin

# Register your models here.
from fees.models import FeeStructure,StudentFee
admin.site.register(FeeStructure)
admin.site.register(StudentFee)