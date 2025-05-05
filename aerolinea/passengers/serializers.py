from rest_framework import serializers
from passengers.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        #fields = ['id', 'name', 'score']
        fields = '__all__'  # This will include all fields in the model


