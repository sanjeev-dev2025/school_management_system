from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from students.models import StudentProfile
from students.serializers import StudentProfileSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics
from accounts.permissions import IsAdminUserOrTeacher, IsAdminUser,IsStudentUser,IsTeacherUser
class StudentProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSerializer
    def get_permissions(self):
        if self.request.method=="POST":
            return [IsAdminUser()]
        else:
            return[IsAuthenticated()]
        

    def get_queryset(self):
        qs=super().get_queryset()
        if not self.request.user.is_staff:
            qs=qs.filter(user=self.request.user)
        return qs