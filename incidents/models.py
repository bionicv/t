from django.db import models
import locations
# Create your models here.
class IncidentType(models.Model):
    name = models.CharField(max_length=30)


class EmergencyLevel(models.Model):
    severity = models.CharField(max_length=30)


class Status(models.Model):
    status_field = models.TextField()


class Incident(models.Model):
    type = models.ForeignKey(IncidentType)
    location = models.ForeignKey(locations.Location)
    time = models.DateTimeField()
    emergency_level = models.ForeignKey(EmergencyLevel)
    length_open = models.IntegerField()
    description = models.TextField()
    status = models.ForeignKey(Status)