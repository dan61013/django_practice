from django.db import models

# Create your models here.

class Bboy(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField()
    power = models.BooleanField(default=False)
    skills = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name