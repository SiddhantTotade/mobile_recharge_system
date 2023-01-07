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