from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializer import *

# Create your views here.
class PlansAPI(APIView):
    def get(self,request):
        all_plans = RechargePlans.objects.all()

        if all_plans:
            plans_serializer = PlanSerializer(all_plans,many=True)
            return JsonResponse(plans_serializer.data,safe=False)
        return JsonResponse("No plans found",safe=False)
    
    def post(self,request):
        plans = PlanSerializer(data=request.data)

        if plans.is_valid():
            plans.save()
            return JsonResponse("Plan added successfully",safe=False)
        return JsonResponse("Failed to add plan",safe=False)

class CustomerAPI(APIView):
    def get(self,request):
        all_customers = Customer.objects.all()

        if all_customers:
            customer_serializer = CustomerSerializer(all_customers,many=True)
            return JsonResponse(customer_serializer.data,safe=False)
        return JsonResponse("No customer found",safe=False)
    
    def post(self,request):
        pass

class RechargeAPI(APIView):
    def get(self,request):
        plans_customer = PlanAndCustomer.objects.all()

        if plans_customer:
            plans_customer_serilaizer = PlanAndCustomerSerializer(plans_customer,many=True)
            return JsonResponse(plans_customer_serilaizer.data,safe=False)
        return JsonResponse("No plans and customer found".data,safe=False)
    
    def post(self,request):
        recharge = PlanAndCustomerSerializer(data=request.data)

        if recharge.is_valid():
            recharge.save()
            return JsonResponse("Recharge successfull",safe=False)
        return JsonResponse("No plans and customer found",safe=False)
