from django.db import models
from django.utils import timezone

class signup(models.Model):
    name = models.CharField()
    place = models.CharField()
    email = models.EmailField()
    mobile = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)

class login(models.Model):
    email = models.EmailField()
    mobile = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)