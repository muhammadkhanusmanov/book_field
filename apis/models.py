from django.db import models
from django.contrib.auth.models import User

class BasicModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class UserPosition(BasicModel):
    position_choices = [
        ('admin','Admin'),
        ('user','User'),
        ('owner','Owner')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='position')
    position = models.CharField(max_length=6, choices=position_choices, default='user')
    
    def __str__(self):
        return self.user.username