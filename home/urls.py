from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("test-404/", views.test_404, name="test_404"),
]
