from django.db import models

# Create your models here.
class RechargePlans(models.Model):
    recharge_plan = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.recharge_plan

class Customer(models.Model):
    taked_plan = models.ForeignKey(RechargePlans,null=True,on_delete=models.CASCADE)
    taked_date = models.DateField()