from rest_framework import serializers
from accounts.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'role',
            'must_change_password',
        ]
        read_only_fields = fields


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'role',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
            },
        }

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role'],
        )

        if user.role == User.Role.STUDENT:
            user.must_change_password = True
        else:
            user.must_change_password = False

        user.save(update_fields=['must_change_password'])

        return user