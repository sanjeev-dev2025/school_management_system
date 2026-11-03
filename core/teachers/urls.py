from django.urls import path
from teachers.views import TeacherProfileListCreateAPIView,TeacherProfileRetrieveUpdateDestoryAPIView
urlpatterns=[
    path('teachercreate/',TeacherProfileListCreateAPIView.as_view(),name='teachercreate'),
    path('teacherupdate/<str:teacher_id>/',TeacherProfileRetrieveUpdateDestoryAPIView.as_view(),name='teacherupdate'),    
]