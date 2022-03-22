from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
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