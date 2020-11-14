from rest_framework import viewsets

from interview_api import serializers
from interview_api.models import User
from interview_api import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
