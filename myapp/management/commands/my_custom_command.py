from django.core.management.base import BaseCommand
from django.utils import timezone
from ... import models
import csv

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        with open('sample.csv') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                data=models.User_details.objects.filter(user_id=row[0])
                if len(data) >0:
                    user_data=models.ActivityPeriod(user=data[0],start_time=row[3],end_time=row[4])
                    user_data.save()
                else:
                    user=models.User_details(real_name=row[1],tz=row[2],user_id=row[0])
                    user.save()
                    user_data=models.ActivityPeriod(user=user,start_time=row[3],end_time=row[4])
                    user_data.save()
