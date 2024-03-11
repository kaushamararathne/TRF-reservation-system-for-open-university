from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.AutoField()
    email = models.EmailField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.namef