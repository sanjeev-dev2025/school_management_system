from django.utils.http import MAX_URL_LENGTH
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models h

def generate_teacher_id():
    year=timezone.localdate().year
    prefix=f"TCH-{year}-"
    last_teacher=(TeacherProfile.objects.filter(teacher_id__startswith=prefix).order_by("-teacher_id").first())
    if last_teacher:
        last_number=int(last_teacher.teacher_id.split('-')[-1])
        new_number=last_number+1
    else:
        new_number=1
    return f"{prefix}{new_number:04d}"

class TeacherProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE="MALE","male"
        FEMALE="FEMALE","female"
        OTHER="OTHER","other"
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='teacherprofile')
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    gender=models.CharField(max_length=6,choices=GenderChoices.choices,null=False)
    address=models.CharField(max_length=50,null=False)
    phone_number=models.CharField(max_length=10,null=False)
    date_of_birth=models.DateField(null=False)
    subject=models.CharField(max_length=50,null=False)
    qualification=models.CharField(max_length=30,null=False)
    joining_date=models.DateField(null=False)
    created_at=models.DateField(null=False)
    teacher_id=models.CharField(max_length=20,null=False,editable=False)
    email=models.EmailField(max_length=50,null=False)
    is_active=models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if not self.teacher_id:
            self.teacher_id=generate_teacher_id()
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
