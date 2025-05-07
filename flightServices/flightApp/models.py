from django.db import models

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10, unique=True)
    operatingAirline = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()
    
class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=20, unique=True)
    phone = models.CharField(max_length=10, unique=True)
   
    
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)


