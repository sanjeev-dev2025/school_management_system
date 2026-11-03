
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUser
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from teachers.models import TeacherProfile
from teachers.serializers import TeacherProfileSerializer

class TeacherProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset=TeacherProfile.objects.all()
    serializer_class=TeacherProfileSerializer
    def get_permissions(self):
        if self.request.method=="POST":
            return[IsAdminUser()]
        return[IsAuthenticated()]
    def get_queryset(self):
        qs=super().get_queryset()
        if self.request.user.role !="ADMIN":
            qs=qs.filter(user=self.request.user)
        return qs
class TeacherProfileRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=TeacherProfile.objects.all()
    serializer_class=TeacherProfileSerializer
    lookup_field="teacher_id"
    def get_permissions(self):
        if self.request.method in ['PUT',"PATCH","DELETE"]:
            return[IsAdminUser()]
        return[IsAuthenticated()]