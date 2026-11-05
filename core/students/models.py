
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
def generate_student_id():
    year=timezone.localdate().year
    prefix=f"STU-{year}-"
    last_student=(StudentProfile.objects.filter(student_id__startswith=prefix).order_by("-student_id").first())
    if last_student:
        last_number=int(last_student.student_id.split('-')[-1])
        new_number=last_number+1
    else:
        new_number=1
    return f"{prefix}{new_number:04d}"


class StudentProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE="MALE","male"
        FEMALE="FEMALE","female"
        OTHER="OTHER","other"
    class Grade(models.TextChoices):
        GRADE_1 = "1", "Grade 1"
        GRADE_2 = "2", "Grade 2"
        GRADE_3 = "3", "Grade 3"
        GRADE_4 = "4", "Grade 4"
        GRADE_5 = "5", "Grade 5"
        GRADE_6 = "6", "Grade 6"
        GRADE_7 = "7", "Grade 7"
        GRADE_8 = "8", "Grade 8"
        GRADE_9 = "9", "Grade 9"
        GRADE_10 = "10", "Grade 10"
        GRADE_11 = "11", "Grade 11"
        GRADE_12 = "12", "Grade 12"

        
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="student_profile")
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    gender=models.CharField(max_length=10,choices=GenderChoices.choices,null=False)
    grade=models.CharField(max_length=2,choices=Grade.choices,null=False)
    year=models.CharField(max_length=20,null=False)
    student_id=models.CharField(max_length=20,null=False,unique=True,editable=False)
    date_of_birth=models.DateField(null=False)
    email=models.EmailField(null=False)
    phone_number=models.CharField(max_length=10,null=False)
    address=models.CharField(max_length=255,null=False)
    admission_date=models.DateField(null=False,auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

       
    def save(self,*args,**kwargs):
        if not self.student_id:
            self.student_id=generate_student_id()
        super().save(*args,**kwargs)
    def __str__(self):
       return f"{self.first_name}-{self.student_id}" 

