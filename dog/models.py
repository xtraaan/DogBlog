from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    dog_name = models.CharField(max_length=20)
    breed = models.TextField()
    weight = models.TextField()
    profile_picture = models.ImageField(upload_to='images/profile_pictures/')

    def __str__(self):
        return self.dog_name