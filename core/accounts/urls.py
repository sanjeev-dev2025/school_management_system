from django.urls import path
from accounts.views import UserListCreateAPIView,CustomLoginView,CustomPasswordChangeView
urlpatterns=[
    path('usercreate/',UserListCreateAPIView.as_view(),name="usercreate"),
    
]