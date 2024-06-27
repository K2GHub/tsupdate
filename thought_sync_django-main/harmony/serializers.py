from rest_framework import serializers
from .models import UserProfile
from core.serializers import UserCreateSerializer, UserSerializer
from core.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ["id", "user", "birthday", "bio", "picture"]
        read_only_fields = ["id"]
    