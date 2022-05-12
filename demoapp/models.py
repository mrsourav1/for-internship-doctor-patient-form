from distutils.command.upload import upload
import email
from types import CoroutineType
from django.db import models
from django.forms import CharField

# Create your models here.
class DemoUser(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100,unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.IntegerField()
    profile_img = models.ImageField(upload_to = 'profileimg',blank = True)
