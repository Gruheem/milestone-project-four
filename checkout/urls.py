from django.urls import path
from . import views, webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('check-order/', views.check_order, name='check_order'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('return/', views.checkout_return, name='checkout_return'),
    path('wh/', webhook.webhook, name='webhook'),
]