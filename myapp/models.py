from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User_details(models.Model):
    user_id=models.CharField(max_length=100)
    real_name=models.CharField(max_length=100)
    tz=models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)


class ActivityPeriod(models.Model):
    user=models.ForeignKey(User_details, on_delete=models.CASCADE)
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)
