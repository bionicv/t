from django.db import models
import locations
import admin
from django.forms import ModelForm

# Create your models here.
class IncidentType(models.Model):
    type_name = models.CharField(max_length=30)


class EmergencyLevel(models.Model):
    severity = models.CharField(max_length=30)


class Status(models.Model):
    status_field = models.TextField()


class Incident(models.Model):
    name = models.CharField(max_length=30)
    incident_type = models.ForeignKey(IncidentType)
    time = models.DateTimeField()
    emergency_level = models.ForeignKey(EmergencyLevel)
    length_open = models.IntegerField()
    description = models.TextField(max_length=1000)
    status = models.ForeignKey(Status)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()

# class IncidentForm(ModelForm):
#     class Meta:
#         model = Incident
#         fields = ['name', 'incident_type', 'time']

### Admin

#class IncidentAdmin(admin.ModelAdmin):
#    search_fields = ["name"]


#admin.site.register(Incident, IncidentAdmin)