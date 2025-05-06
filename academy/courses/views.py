from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Course
from courses.serializer import CourseSerializer
from rest_framework import status

from rest_framework import generics, mixins

from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

"""
class CourseList(generics.ListCreateAPIView):  
    queryset = Course.objects.all()  # fixed name to be used by mixing methods
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
"""
    
"""
class CourseList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Course.objects.all()  # fixed name to be used by mixing methods
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
    
class CourseDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self, request,pk ):
        return self.update(request,pk)

    def delete(self, request,pk):
        return self.destroy(request,pk)

    
"""

"""

class CourseList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return None

    def get(self, request, id):
        course = self.get_object(id)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = self.get_object(id)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""