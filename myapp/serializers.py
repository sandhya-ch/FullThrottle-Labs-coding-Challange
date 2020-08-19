from rest_framework import serializers
from myapp.models import User,ActivityPeriod

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model=ActivityPeriod
        fields='__all__'