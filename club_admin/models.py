from django.db import models
from event_details.models import Event_Details
from django.contrib.auth import get_user_model
from accounts.models import*
user = get_user_model()
# Create your models here.
class Registration(models.Model):
    event = models.ForeignKey('event_details.Event_Details', on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey(user,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} for {self.event}"