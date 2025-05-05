from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee


# Function-based view
def employeeView(request):
    emp = {
        'id':13,
        'name':'John Doe',
        'age':30,
        'department':'HR',
        'salary':50000
    }

    data = Employee.objects.all() # Query all employees from the database

    response = {'employees':list(data.values('name','salary'))} # Initialize response dictionary

    #return JsonResponse(emp) # Serialize data to JSON
    return JsonResponse(response) # Serialize data to JSON