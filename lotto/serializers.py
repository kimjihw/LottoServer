from django.contrib.auth.password_validation import validate_password
from django.template.base import Token
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from lotto.models import Lotto, Weekend


class LottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotto
        fields = '__all__'

class WeekendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekend
        fields = '__all__'