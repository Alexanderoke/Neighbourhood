from django.db import models
from django.contrib.auth.models import User
from hood.models import *
from django.forms import CharField
# Create your models here.


class Profile(models.Model):
  name = models.CharField(max_length=200)
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
  profile_image =models.ImageField(upload_to='images/')  


def __str__(self):
  return f'{self.user.username} Profile'