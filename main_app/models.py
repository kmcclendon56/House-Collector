
from django.db import models
from django.urls import reverse


# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=100)
    rooms_baths = models.CharField(max_length=10)
    sqft = models.IntegerField()
    gas_stove = models.BooleanField(default=False)
    notes = models.CharField(max_length=300)
    allows_dogs = models.BooleanField()


    def get_absolute_url(self):
        return reverse('detail', kwargs={'house_id': self.id})