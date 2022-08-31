
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


CITY = (
    ('A', 'Austin'),
    ('R', 'Round Rock'),
    ('P', 'Pflugerville'),
    ('C', 'Cedar Park'),
)

class Location(models.Model):
    city = models.CharField(
        max_length=1,
            choices=CITY,
            default=CITY[0][0]
        )
    neighborhood = models.CharField(max_length=100)

    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_city_display()} on {self.city}"