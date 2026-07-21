from django.urls import path
from . import views

urlpatterns = [
    # End point for getting possible attributes for the products admin
    path('get-attributes/', views.get_attributes, name='get_attributes'),
    path('get-attribute-values/', views.get_attribute_values, name='get_attribute_values'),
]