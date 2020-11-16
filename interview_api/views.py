from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListCreateAPIView
from collections import OrderedDict

from interview_api import serializers
from interview_api.models import User, InterviewSlot
from interview_api import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)


class InterviewSlotViewSet(viewsets.ModelViewSet):
    """Handle creating and updating interview slots"""
    serializer_class = serializers.InterviewSlotSerializer
    queryset = InterviewSlot.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)


class ActiveSlotList(ListCreateAPIView):
    """To get the specific interview slots by passing interviewer_id and candidate_id as query parameters"""
    queryset = InterviewSlot.objects.all()
    serializer_class = serializers.InterviewSlotSerializer

    def list(self, request):
        """
        List active interview slots by passing interviewer_id and candidate_id as query parameters
        """
        interviewer_id = request.query_params.get('interviewer_id', None)
        candidate_id = request.query_params.get('candidate_id', None)
        if not interviewer_id:
            raise ParseError('Please provide interviewer_id as query parameter')
        if not candidate_id:
            raise ParseError('Please provide candidate_id as query parameter')

        candidate_json = self.get_formatted_json(candidate_id, is_candidate=True)
        interviewer_json = self.get_formatted_json(interviewer_id, is_interviewer=True)
        serialized_data = self.format_serialized_data(candidate_json, interviewer_json)
        return Response(serialized_data)

    def get_formatted_json(self, user_id, is_interviewer=False, is_candidate=False):
        """Get the formated json , like date : [slot1, slot2] for candidate and interviewer"""
        result = {}
        user_json_list = self.get_queryset().filter(
                user_id=user_id,
                user__is_interviewer=is_interviewer,
                user__is_candidate=is_candidate
            ).values('id', 'slot', 'date')
        for user_json in user_json_list:
            date_string = user_json['date'].strftime("%Y-%m-%d")
            slot = [choice[1] for choice in InterviewSlot.SLOT_CHOICES if choice[0] == user_json['slot']][0]
            if date_string in result.keys():
                result[date_string].append(slot)
            else:
                result[date_string] = [slot]
        return result

    def format_serialized_data(self, interviewer_json, candidate_json):
        """Intersection of candidate json and interviwer json to get the expected output"""
        response_json = OrderedDict()
        for key in interviewer_json.keys():
            slots = []
            if key in candidate_json:
                slots = [slot for slot in candidate_json[key] if slot in interviewer_json[key]]
            if slots:
                slots.sort()
                response_json[key] = slots
        return response_json
