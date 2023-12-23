from django.urls import path
from . import views

urlpatterns = [

    path('edit_tenant/', views.edit_tenant, name='edit_tenant'),
    path('view_tenant/', views.view_tenant_profile, name='view_tenant'),
    path('property_list/', views.property_list, name='property_list'),
    path('assign_unit/<int:pk>', views.assign_unit_to_tenant, name='assign_unit'),

]