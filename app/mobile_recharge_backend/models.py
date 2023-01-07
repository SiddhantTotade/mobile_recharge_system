from django.db import models

# Create your models here.
class RechargePlans(models.Model):
    plan_name = models.CharField(max_length=20,null=True,blank=True)
    plan_cost=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.plan_cost)

class Customer(models.Model):
    customer_name=models.CharField(max_length=20,null=True,blank=True)
    taked_date=models.DateField()
    
    def __str__(self):
        return str(self.customer_name)

class PlanAndCustomer(models.Model):
    plans = models.ForeignKey(RechargePlans,null=True,blank=True,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)