from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializers import UserSerializer,ActivityPeriodSerializer
from myapp.models import User,ActivityPeriod

# Create your views here.
class Userviewset(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


class ActivityPeriodviewset(viewsets.ModelViewSet):
    serializer_class=ActivityPeriodSerializer
    queryset=ActivityPeriod.objects.all()