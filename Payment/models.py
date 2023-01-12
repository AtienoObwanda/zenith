from django.db import models

class MobilePayment(models.Model):
    phone_number = models.IntegerField(blank=False, null=True)
    
# class PaypalPayment(models.Model):
#     pass

# class cardPayment(models.Model):
#     pass

# class Shipping(models.Model):
#     pass