from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.db.models import Q

from interview_api import serializers
from interview_api.models import User,InterviewSlot
from interview_api import permissions



class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)


class InterviewSlotViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.InterviewSlotSerializer
    queryset = InterviewSlot.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
