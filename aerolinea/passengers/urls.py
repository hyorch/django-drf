
from django.urls import path
from passengers import views

urlpatterns = [ 
    path('', views.getPassengerList),
    path('<int:pk>/', views.getPassengerDetail),
]