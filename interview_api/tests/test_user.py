from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def test_create_interviewer(self):
        """Test creating a new user"""
        email = "test@gmail.com"
        username = "test"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password,
            is_candidate=False,
            is_interviewer=True
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_candidate(self):
        """Test creating a new user"""
        email = "test@gmail.com"
        username = "test"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password,
            is_candidate=True,
            is_interviewer=False
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating a newm super user"""
        username = "test"
        password = "test1234"
        user = get_user_model().objects.create_superuser(
            username=username,
            password=password,
        )
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
