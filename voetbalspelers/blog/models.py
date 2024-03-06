from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class voetbalspelers(models.Model):
    naam_voetballer = models.CharField(max_length=50)
    actuele_voetbalclub = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def ___str___(self):
    return self.title
