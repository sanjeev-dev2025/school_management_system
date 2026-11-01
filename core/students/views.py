from django.shortcuts import render
from students.models import StudentProfile
from students.serializers import StudentProfileSerializer
# Create your views here.
from rest_framework import generics

class StudentProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSerializer
    def get_permissions(self):
        if self.request.method=="POST":
            return []

