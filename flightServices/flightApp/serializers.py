from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re

def isFlightNumberValid(data):
    print("isFlightNumberValid called")
    if(re.match("^[a-zA-Z0-9]*$",data['flightNumber'])==None):
        raise serializers.ValidationError("Invalid Flight Number. Flight number must be alphanumeric.")
    #return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]

    #   validate_fieldToValidate
    def validate_flightNumber(self, flightNumer):
        print("Validating flight number")
        if(re.match("^[a-zA-Z0-9]*$",flightNumer)==None):
            raise serializers.ValidationError("Invalid Flight Number. Flight number must be alphanumeric.")
        return flightNumer
    
    def validate(self, data):
        print("Validating flight data")
        if data['departureCity'] == data['arrivalCity']:
            raise serializers.ValidationError("Departure city and arrival city cannot be the same.")
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    #flight = FlightSerializer()
    #passenger = PassengerSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'

   