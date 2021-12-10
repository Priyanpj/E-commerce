from django.db import models
from shopapp.models import *
# Create your models here.
class cartlist(models.Model):
    def __str__(self):
        return self.cart_id
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
class items(models.Model):
    def __str__(self):
        return self.prodt
    prodt=models.ForeignKey(feature_products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def total(self):
        return self.prodt.price*self.quantity