from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(RechargePlans)
admin.site.register(Customer)
admin.site.register(PlanAndCustomer)
# class ChooseCustomerPlans(admin.StackedInline):
#     model = RechargePlans

# @admin.register(Customer)
# class CustomerPlans(admin.ModelAdmin):
#     inlines = [ChooseCustomerPlans]

#     class Meta:
#         model = Customer

# @admin.register(RechargePlans)
# class OptedPlans(admin.ModelAdmin):
#     pass