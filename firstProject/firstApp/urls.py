from django.urls import path
from firstApp import views

urlpatterns = [   
    path('employees/', views.employeeView),
]