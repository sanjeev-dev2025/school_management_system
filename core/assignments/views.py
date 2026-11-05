
from django.shortcuts import render
from rest_framework import generics
from accounts.permissions import IsTeacherUserOrStudent,IsTeacherUser,IsStudentUser
from assignments.serializers import AssignmentSubmissionSerializer,AssignmentSerializer
# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from assignments.models import Assignment,AssignmentSubmission
class AssignmentListCreateAPIView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer
    def get_permissions(self):
        if self.request.method=="POST":
            return[IsTeacherUser()]
        return [IsTeacherUserOrStudent()]
    def perform_create(self, serializer):
        serializer.save(
            teacher=self.request.user.teacherprofile
        )
class AssignmentRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSubmissionSerializer
    permission_classes=[IsTeacherUser]
    def get_queryset(self):
        qs=super().get_queryset()
        if self.request.role !="ADMIN":
            qs=qs.filter(user=self.request.user)
        return qs
class AssignmentSubmissionListCreateAPIView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset=AssignmentSubmission.objects.all()
    serializer_class=AssignmentSubmissionSerializer
    def get_permissions(self):
        if self.request.method=="POST":
            return[IsStudentUser()]
        return[IsTeacherUser()]
    def get_queryset(self):
        qs=super().get_queryset()
        if self.request.role !="ADMIN":
            qs=qs.filter(user=self.request.user)
        return qs
class AssignmentSubmissionRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]   
    queryset=AssignmentSubmission.objects.all()
    serializer_class=AssignmentSubmissionSerializer
    permission_classes=[IsTeacherUser]
    def get_queryset(self):
        qs=super().get_queryset()
        if self.request.role !="ADMIN":
            qs=qs.filter(user=self.request.user)
        return qs    
    