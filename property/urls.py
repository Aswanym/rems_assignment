from django.urls import path
from . import views

urlpatterns = [
    path('create_property/', views.property_create, name='create_property'),
    path('create_unit/<int:pk>/', views.unit_create, name='create_unit'),
    path('property_profile/<int:pk>/', views.view_property_profile, name='property_profile')

]