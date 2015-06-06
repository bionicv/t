from django.db import models

# Create your models here.
class EventLocation(models.Model):
    name = models.CharField(max_length=30)
    suburb = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    parking = models.CharField(max_length=30)

class EventType(models.Model):
    name = models.CharField(max_length=30)

class Event(models.Model):
    location = models.ForeignKey(EventLocation)
    cost = models.CharField(max_length=30)
    description = models.TextField()
    # Resources = models.
    # Amenities = models.
