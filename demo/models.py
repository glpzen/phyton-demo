from django.db import models


# Create your models here.

class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=8)

    class Meta:
        db_table = "vehicles"


class NavigationRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, related_name="records", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = "navigation_records"
