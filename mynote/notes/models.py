from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    note=models.TextField()
    image=models.ImageField(upload_to='uploads',blank=True)
    time_created=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    user=models.IntegerField()

    def __str__(self):
        return self.note

class UserAccount(models.Model):
    user=models.CharField(max_length=300)
    image=models.ImageField(upload_to='uploads',blank=True)

    def __str__(self):
        return self.user
