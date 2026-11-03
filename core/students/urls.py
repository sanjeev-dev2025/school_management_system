from django.urls import path
from students.views import StudentProfileListCreateAPIView,StudentProfileRetrieveUpdateDestroyAPIView
urlpatterns=[
    path('studentcreate/',StudentProfileListCreateAPIView.as_view(),name="studentcreate"),
    path('studentupdate/<str:student_id>/',StudentProfileRetrieveUpdateDestroyAPIView.as_view(),name="studentupdate"),
]