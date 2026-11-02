from rest_framework import generics

from accounts.models import User
from accounts.serializers import (
    UserCreateSerializer,
    UserProfileSerializer,
)

from accounts.permissions import (
    IsAdminUser,
    IsAdminUserOrTeacher,
)

from dj_rest_auth.views import LoginView, PasswordChangeView


class UserListCreateAPIView(generics.ListCreateAPIView):

    queryset = User.objects.all()

    def get_serializer_class(self):

        if self.request.method == "POST":
            return UserCreateSerializer

        return UserProfileSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUser()]

        return [IsAdminUserOrTeacher()]

    def get_queryset(self):

        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            queryset = queryset.filter(
                id=self.request.user.id
            )

        return queryset


class CustomLoginView(LoginView):

    def get_response(self):

        response = super().get_response()

        user = self.user

        response.data["id"] = user.id
        response.data["username"] = user.username
        response.data["role"] = user.role
        response.data["must_change_password"] = (
            user.must_change_password
        )

        return response


class CustomPasswordChangeView(PasswordChangeView):

    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:

            request.user.must_change_password = False

            request.user.save(
                update_fields=["must_change_password"]
            )

        return response