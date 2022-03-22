from django.db import models
from django.contrib.auth.models import User
from hood.models import *

# Create your models here.


class Profile(models.Model):
  email = models.EmailField(max_length=100)
  name = models.CharField(max_length=200)
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
  profile_image =models.ImageField(upload_to='images/')  


def __str__(self):
  return f'{self.user.username} Profile'


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')
    
            
    def __str__(self):
        return f'{self.title} Post'
    
    def delete_post(self):
        self.delete()