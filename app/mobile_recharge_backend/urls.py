from django.urls import path
from .views import *

urlpatterns = [
    path('plans/',PlansAPI.as_view())
]