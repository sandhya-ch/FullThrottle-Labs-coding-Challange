from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    real_name=models.CharField(max_length=100)
    tz=models.CharField(max_length=100)

    def __str__(self):
        return self.id

class ActivityPeriod(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return str(self.user)
