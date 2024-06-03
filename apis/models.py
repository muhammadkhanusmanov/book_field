from django.db import models
from django.contrib.auth.models import User

class BasicModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True



