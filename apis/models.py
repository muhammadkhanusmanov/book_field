from django.contrib.auth.models import AbstractUser
from django.db import models

class BasicModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class ProUser(AbstractUser):
    position_choices = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('owner', 'Owner')
    ]
    
    position = models.CharField(max_length=10, choices=position_choices, default='user')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='pro_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='pro_users',
        blank=True
    )

    def __str__(self):
        return self.username