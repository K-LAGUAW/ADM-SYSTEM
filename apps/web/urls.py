from . import views
from django.urls import path

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('home/', views.home, name='home'),
    path('shipments/', views.shipments, name='shipments'),
]