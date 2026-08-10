from django.urls import path
from . import views # webhooks

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('return/', views.checkout_return, name='checkout_return'),
    # path('wh/', webhooks.webhook, name='webhook'),
]