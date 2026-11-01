
from django.db import models
from django.conf import settings
# Create your models here.
class StudentProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE="MALE","male"
        FEMALE="FEMALE","female"
        OTHER="OTHER","other"
    class FacultyChoices(models.TextChoices):
        BIT="BIT","bit"
        BBA="BBA","bba"
        BCA="BCA","bca"
        BIM="BIM","bim"
        BSC="BSC","bsc"
        BBS="BBS","bbs"
        BSCSIT="BSCSIT","bscsit"

    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="student_profile")
    gender=models.CharField(max_length=10,choices=GenderChoices.choices,null=False)
    faculty=models.CharField(max_length=10,choices=FacultyChoices.choices,null=False)
    year=models.CharField(max_length=20,null=False)
    student_id=models.CharField(max_length=20,null=False,unique=True)
    date_of_birth=models.DateField(null=False)
    phone_number=models.CharField(max_length=15,null=False)
    address=models.CharField(max_length=255,null=False)
    profile_photo=models.ImageField(upload_to='student_photos/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    class Meta:
        ordering=["-student_id"]
    def __str__(self):
       return f"{self.user.get_full_name()}-{self.student_id}-{self.faculty}"    