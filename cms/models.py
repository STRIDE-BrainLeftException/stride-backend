from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property



class GalacticUser(AbstractUser):
    galactic_id = models.CharField(max_length=256, null=True)


class Planet(models.Model):
    name = models.CharField(max_length=256)
    # coords are in light years
    x_coord = models.BigIntegerField()
    y_coord = models.BigIntegerField()
    z_coord = models.BigIntegerField()
    planet_tax_rate = models.FloatField()
    description = models.JSONField(null=True)

    def calculate_distance(self, other_planet):
        return (
            (self.x_coord - other_planet.x_coord) ** 2
            + (self.y_coord - other_planet.y_coord) ** 2
            + (self.z_coord - other_planet.z_coord) ** 2
        ) ** 0.5


class ShipType(models.Model):
    name = models.CharField(max_length=256)
    price_multiplier = models.FloatField()
    base_price = models.FloatField()
    description = models.JSONField(null=True)

    def calculate_price(self, distance):
        return self.base_price + (distance * self.price_multiplier)


class Package(models.Model):
    name = models.CharField(max_length=256)
    description = models.JSONField(null=True)
    price_multiplier = models.FloatField()
    base_price = models.FloatField()

    def calculate_price(self, distance):
        return self.base_price + (distance * self.price_multiplier)


class Booking(models.Model):
    user = models.ForeignKey(GalacticUser, on_delete=models.CASCADE)
    start_planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name="start_planet"
    )
    end_planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, related_name="end_planet"
    )
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    ship_type = models.ForeignKey(ShipType, on_delete=models.CASCADE)
    seat_count = models.IntegerField()
    journey_date = models.DateField()
    booking_price = models.FloatField()
    details = models.JSONField(null=True)

    @cached_property
    def calculated_price(self):
        distance = self.start_planet.calculate_distance(self.end_planet)
        ship_price = self.ship_type.calculate_price(distance)
        package_price = self.package.calculate_price(distance)
        return ship_price + package_price

    @cached_property
    def tax_price(self):
        return self.calculated_price * self.end_planet.planet_tax_rate

    @cached_property
    def total_price(self):
        return self.calculated_price + self.tax_price
    
class TumorDetection(models.Model):
    path = models.CharField(max_length=1024)
    detection_class = models.CharField(max_length=256)
    trained = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)

