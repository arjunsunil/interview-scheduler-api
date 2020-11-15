from django.contrib.auth.models import BaseUserManager
from rest_framework.exceptions import ParseError


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, password, is_candidate, is_interviewer):
        """create and saves a new user"""
        if is_candidate == is_interviewer:
            raise ParseError('User must be candidate or interviewer')
        user = self.model(
            email=email,
            username=username,
            is_candidate=is_candidate,
            is_interviewer=is_interviewer
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        """create and saves a new super user"""
        user = self.model(
            username=username,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user
