from . import views
from django.urls import path

urlpatterns = [
    path('customers/', views.customers, name='customers')
]