from django.test import TestCase
from django.contrib.auth import get_user_model
from interview_api.models import InterviewSlot


class InterviewSlotTest(TestCase):

    def test_create_slot_for_interviewer(self):
        """Test creating a new slot"""
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

        date = '2020-1-2'
        slot = 1
        interview_slot = InterviewSlot.objects.create(
            date=date,
            slot=slot,
            user=user
        )

        self.assertEqual(interview_slot.date, date)
        self.assertEqual(interview_slot.slot, slot)

    def test_create_slot_for_candidate(self):
        """Test creating a new slot"""
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
        date = '2020-1-2'
        slot = 1
        interview_slot = InterviewSlot.objects.create(
            date=date,
            slot=slot,
            user=user
        )

        self.assertEqual(interview_slot.date, date)
        self.assertEqual(interview_slot.slot, slot)
