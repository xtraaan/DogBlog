from django.db import models
from django.contrib.auth.models import User
from dog.models import Dog

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    dog = models.ManyToManyField(Dog)

    def __str__(self):
        return self.name