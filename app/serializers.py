import sys
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.db import transaction


class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source='pk')
    name = serializers.CharField(required=True)
    api_key = serializers.CharField(read_only=True)
    class Meta:
        model = models.Appication
        fields = (
            'id',
            'name',
            'api_key'
        )