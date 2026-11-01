from django.urls import path
from students.views import StudentProfileListCreateAPIView
urlpatterns=[
    path('studentcreate/',StudentProfileListCreateAPIView.as_view(),name="studentcreate"),
]