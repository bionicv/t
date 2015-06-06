from django.db import models
import admin
# Create your models here.
class EventLocation(models.Model):
    name = models.CharField(max_length=30)
    suburb = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    parking = models.CharField(max_length=30)

class EventType(models.Model):
    name = models.CharField(max_length=30)

class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(EventLocation)
    cost = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField()
    # Resources = models.
    # Amenities = models.

    def __unicode__(self):
        return "%s at %s, %s" %(self.name, self.location.name, self.date.year)

### Admin

class IncidentAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Event, EventAdmin)