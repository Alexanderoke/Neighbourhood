from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
  NeighbourhoodName= models.CharField(max_length=100)
  NeighbourHoodLocation = models.CharField(max_length=200)
  OccupantsCount = models.IntegerField()
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_NeighbourhoodName="hood",null=True)
