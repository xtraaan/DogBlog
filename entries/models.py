from django.db import models
from django.contrib.auth.models import User
from dog.models import Dog
from person.models import Person
# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/', blank = True, null = True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.title