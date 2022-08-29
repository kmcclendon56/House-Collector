from django.db import models

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=100)
    rooms_baths = models.CharField(max_length=10)
    sqft = models.IntegerField()
    gas_stove = models.BooleanField()
    notes = models.CharField(max_length=300)
    allows_dogs = models.BooleanField()