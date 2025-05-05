from rest_framework import serializers
from fbvApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'score']
        # fields = '__all__'  # This will include all fields in the model


