from django.db import models
from django.contrib.auth.models import User



class customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=100)
    GST=models.CharField(max_length=20)

