from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




class StudentPagination(PageNumberPagination):
    page_size = 4   

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #pagination_class = StudentPagination
    pagination_class = LimitOffsetPagination
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name', 'score']  # Add any fields you want to filter by
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['id', 'score']  # Add any fields you want to order by
    search_fields = ['name', 'id']  # Add any fields you want to search by
    ordering = ['id']  # Default ordering
    


""" 
class StudentList(generics.ListCreateAPIView):  
    queryset = Student.objects.all()  # fixed name to be used by mixing methods
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


""" 

""" 

class StudentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Student.objects.all()  # fixed name to be used by mixing methods
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
    
class StudentDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self, request,pk ):
        return self.update(request,pk)

    def delete(self, request,pk):
        return self.destroy(request,pk)


""" 



""" 

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        student = self.get_object(pk)        
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = self.get_object(pk)        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):  
        student = self.get_object(pk)        
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""