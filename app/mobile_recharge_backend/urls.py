from django.urls import path
from .views import *

urlpatterns = [
    path('plans/',PlansAPI.as_view()),
    path('customers/',CustomerAPI.as_view()),
    path('customer/<int:pk>',SpecificPlansAndCustomer.as_view()),
    path('recharges/',RechargeAPI.as_view()),
]