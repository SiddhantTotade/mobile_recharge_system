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
        plans = RechargePlans.objects.create(recharge_plan=validated_data['recharge_plan'],customer=validated_data['customer'],taked_date=validated_data['taked_date'])
        return plans