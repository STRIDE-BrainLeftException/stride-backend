from django.contrib.auth.models import AbstractUser
from django.db import models


class GalacticUser(AbstractUser):
    galactic_id = models.CharField(max_length=256, null=True)


# class Planet(models.Model):
#     name = models.CharField(max_length=256)
#     galaxy = models.CharField(max_length=256)
#     places_to_visit = models.JSONField(null=True)
