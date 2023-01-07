from django.urls import path
from .views import *

urlpatterns = [
    path('plans/',PlansAPI.as_view()),
    path('customer/',CustomerAPI.as_view()),
    path('recharge/',RechargeAPI.as_view()),
]