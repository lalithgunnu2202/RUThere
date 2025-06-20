from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.
class Event_Details(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(editable=True,auto_now=True)
    time = models.TimeField(editable=True,auto_now=True)
    location = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    price = models.CharField(max_length=5)
    img_url = models.TextField(max_length=500)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} by {self.host}"