
from django.urls import path, include
from customers import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]



"""
urlpatterns = [

    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>', views.CustomerDetail.as_view(), name='customer-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order-detail'),
]

"""