from django.db import models

class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    travelPoints = models.IntegerField(max_length=6)

    def __str__(self):
        return self.id+" " + self.firstName + " " + self.lastName + " " + self.travelPoints
    

