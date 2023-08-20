from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ship(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.ship} to {self.planet} on {self.date}"
