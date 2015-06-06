from django.db import models

# Create your models here.
class LocationType(models.Model):
    name = models.CharField(max_length=30)


class LocationAdministrator(models.Model):
    name = models.CharField(max_length=30)


class Status(models.Model):
    status_field = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(LocationType)
    administrator = models.ForeignKey(LocationAdministrator)
    # Resources = models.
    # Amenities = models.
