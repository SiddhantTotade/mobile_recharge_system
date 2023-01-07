from django.contrib import admin
from .models import *

# Register your models here.
class ChooseCustomerPlans(admin.StackedInline):
    model = Customer

@admin.register(Customer)
class CustomerPlans(admin.ModelAdmin):
    pass