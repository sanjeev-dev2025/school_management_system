from rest_framework import serializers
from django.db import transaction 
from students.models import StudentProfile
from accounts.models import User
import string
import secrets
from students.utils import send_student_credentials
class StudentProfileSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(source="user.email")
    student_id=serializers.ReadOnlyField()
    class Meta:
        model=StudentProfile
        fields=[
            'first_name','last_name','student_id','gender','year','date_of_birth','email','address','phone_number','admission_date'
        ]

    def password_generator(self):
        password=''.join(secrets.choice(string.ascii_letters+string.digits)for i in range(10))
        return password
    @transaction.atomic
    def create(self,validated_data):
        user_data=validated_data.pop('user')
        email=user_data["email"]
        password=self.password_generator()
        
        user=User.objects.create_user(
            username=validated_data['first_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=email,
            role=User.Role.STUDENT,
            password=password,
            must_change_password=True,
               

            )
        student=StudentProfile.objects.create(
            user=user,
            **validated_data
        )
        send_student=send_student_credentials(student,password)
        return student
    @transaction.atomic
    def update(self, instance, validated_data):

        user_data = validated_data.pop("user", {})

        if "email" in user_data:
            instance.user.email = user_data["email"]
            instance.user.save(update_fields=["email"])

        return super().update(instance, validated_data)

