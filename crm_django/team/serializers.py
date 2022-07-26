from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        
class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            'id', 
            'name', 
            'members'
        )