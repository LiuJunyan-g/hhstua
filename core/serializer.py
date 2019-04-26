from rest_framework import serializers
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "pwd", 'role')


class PredictionListSerializer(serializers.ModelSerializer):
    create_on = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ("id", "create_on", "name", "sex", "age", "major", "department", "academy", "location", "user_id")

    def get_create_on(self, obj):
        return str(obj.create_on)[:10] + ' ' + str(obj.create_on)[11:16]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'county')
