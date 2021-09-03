from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User

from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the project object"""

    class Meta:
        model = Project
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
