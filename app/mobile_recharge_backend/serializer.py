from .models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        customer = Customer.objects.create(customer_name=validated_data['customer_name'])
        customer.save()
        return customer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RechargePlans
        fields = '__all__'

    def create(self, validated_data):
        plans = RechargePlans.objects.create(plan_name=validated_data['plan_name'],plan_cost=validated_data['plan_cost'])
        return plans

class PlanAndCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAndCustomer
        fields = '__all__'

    def create(self, validated_data):
        plans_and_customer = PlanAndCustomer.objects.create(plans=validated_data['plans'],customer=validated_data['customer'],taked_date=validated_data['taked_date'])
        return plans_and_customer