from rest_framework import serializers

from interview_api.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializers for a user profile object """
    candidate = serializers.BooleanField(source='is_candidate')
    interviewer = serializers.BooleanField(source='is_interviewer')

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'candidate', 'interviewer')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_candidate=validated_data['is_candidate'],
            is_interviewer=validated_data['is_interviewer']
            )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""

        if 'is_candidate' in validated_data:
            raise serializers.ValidationError({
                'candidate': 'You must not change this field.',
            })
        if 'is_interviewer' in validated_data:
            raise serializers.ValidationError({
                'interviewer': 'You must not change this field.',
            })
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

