from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from chat.models import *


class RegistrationSerializer(serializers.Serializer):
    pass
