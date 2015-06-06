from django.db import models
import locations
import admin
# Create your models here.
class IncidentType(models.Model):
    name = models.CharField(max_length=30)


class EmergencyLevel(models.Model):
    severity = models.CharField(max_length=30)


class Status(models.Model):
    status_field = models.TextField()


class Incident(models.Model):
    name = models.CharField(max_length=30)
    incident_type = models.ForeignKey(IncidentType)
    location = models.ForeignKey(locations.Location)
    time = models.DateTimeField()
    emergency_level = models.ForeignKey(EmergencyLevel)
    length_open = models.IntegerField()
    description = models.TextField(max_length=1000)
    status = models.ForeignKey(Status)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()


### Admin

class IncidentAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Incident, IncidentAdmin)