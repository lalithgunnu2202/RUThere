from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.TextField()

    def __str__(self):
        return self.name