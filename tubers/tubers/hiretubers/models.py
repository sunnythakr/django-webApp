from django.db import models
from datetime import datetime



# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    tuber_id = models.CharField(max_length=100)
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateField(blank=True, default=datetime.now)