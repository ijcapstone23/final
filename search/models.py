from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=248)
    shop_name = models.CharField(max_length=59)
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=59248, default=None, null=True)
    url = models.CharField(max_length=2480)
    imgurl = models.CharField(max_length=2480, default=None, null=True)
    star = models.FloatField(default=3.0)

    def __str__(self):
        return model_to_dict(self)
    
class Basket(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return model_to_dict(self)
