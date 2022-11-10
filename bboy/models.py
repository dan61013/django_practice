from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bboy(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField()
    power = models.BooleanField(default=False)
    skills = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    # from django.contrib.auth.models import User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    orangization = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.username