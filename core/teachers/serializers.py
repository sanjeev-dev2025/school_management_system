from django.core.validators import validate_email
from django.db import transaction
from teachers.models import TeacherProfile
from rest_framework import serializers
import string
import secrets
from accounts.models import User
from teachers.utils import send_teacher_credentials
class TeacherProfileSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(source='user.email')
    teacher_id=serializers.ReadOnlyField()
    class Meta:
        
        model=TeacherProfile
        fields=[
            'id','first_name','last_name','email','teacher_id','gender','date_of_birth','phone_number','created_at','joining_date'
            ,'address','subject','qualification'
        ]
    def password_generator(self):
        password=''.join(secrets.choice(string.ascii_letters+string.digits) for i in range(10))
        return password

    @transaction.atomic
    def create(self,validated_data):
        user_data=validated_data.pop('user')
        email=user_data['email']
        password=self.password_generator()
        user=User.objects.create_user(
            username=validated_data['first_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=email,
            role=User.Role.TEACHER,
            password=password,
            must_change_password=True,

        )
        teacher=TeacherProfile.objects.create(
            user=user,
            **validated_data
        )
        password=send_teacher_credentials(teacher,password)
        return teacher
    @transaction.atomic
    def update(self,instance,validated_data):
        user_data=validated_data.pop('user',{})
        if "email" in user_data:
            instance.user.email=user_data["email"]
            instance.user.save(update_fields=['email'])
        return super().update(instance,validated_data)
