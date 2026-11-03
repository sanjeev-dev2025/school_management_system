from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN","admin"
        STUDENT="STUDENT","student"
        TEACHER="TEACHER","teacher"
    
    role=models.CharField(max_length=20,choices=Role.choices)
    email=models.EmailField()
    must_change_password=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}"