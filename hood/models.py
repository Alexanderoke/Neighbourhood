from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.
class NeighbourHood(models.Model):
  NeighbourHood_Id =IntegerField()
  NeighbourhoodName= models.CharField(max_length=100)
  NeighbourHoodLocation = models.CharField(max_length=200)
  OccupantsCount = models.IntegerField()
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_NeighbourhoodName="hood",null=True)


def __str__(self):
  return self.NeighbourhoodName

def create_neighborhood(self):
    self.save()

def delete_neighborhood(self):
    self.delete()
        
def update_neighborhood(self):
     self.update()
def update_occupants(self):
    self.update()  

@classmethod
def find_neighborhood(cls, neighborhood_id):
    return cls.objects.filter(id=neighborhood_id)


class Bussiness(models.Model):
  Business_name = models. CharField(max_length=200)
  Business_email = models.EmailField(max_length=200)
  NeighbourHood_Id = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')

def __str__(self):
  return self.Business_name

def create_business(self):
        self.save()

def delete_business(self):
  self.delete()

@classmethod
def search_business(cls, name):
  return cls.objects.filter(name__icontains=name).all()