from django.urls import path
from assignments.views import (
    AssignmentSubmissionListCreateAPIView,AssignmentListCreateAPIView,
    AssignmentRetrieveUpdateDestoryAPIView,
    AssignmentSubmissionRetrieveUpdateDestoryAPIView
)
urlpatterns=[
    path('assignment/',AssignmentListCreateAPIView.as_view(),name="assignment"),
    path('assignmentupdate/<int:id>/',AssignmentRetrieveUpdateDestoryAPIView.as_view(),name="assignmentupdate"),
    path('assignmentsubmission/',AssignmentSubmissionListCreateAPIView.as_view(),name="assignmentsubmission"),
    path('submissionupdate/<int:id>',AssignmentSubmissionRetrieveUpdateDestoryAPIView.as_view(),name="submissionupdate")
]