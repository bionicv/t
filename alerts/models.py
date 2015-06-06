from django.db import models
import admin
import locations
# Create your models here.
class AlertType(models.Model):
    name = models.CharField(max_length=30)


class EmergencyLevel(models.Model):
    severity = models.CharField(max_length=30)


class Status(models.Model):
    status_field = models.TextField()


class Alert(models.Model):
    name = models.CharField(max_length=30)
    incident_type = models.ForeignKey(AlertType)
    location = models.ForeignKey(locations.Location)
    time = models.DateTimeField()
    emergency_level = models.ForeignKey(EmergencyLevel)
    length_open = models.IntegerField()
    description = models.TextField(max_length=1000)
    status = models.ForeignKey(Status)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()

    def get_absolute_url(self):
        return ('view_alert', None, { 'alert': self.name })


### Admin

class AlertAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Alert, AlertAdmin)