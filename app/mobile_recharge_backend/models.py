from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class RechargePlans(models.Model):
    recharge_plan = models.IntegerField(null=True,blank=True)
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    taked_date = models.DateField()
