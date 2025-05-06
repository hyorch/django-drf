# Serializer for Course Class
from rest_framework import serializers
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'rating']
        # fields = '__all__'  # This will include all fields in the model

