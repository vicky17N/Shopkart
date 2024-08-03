from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def GetFileName(req,FileName):
    Now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    NewFileName = '%s%s'%(Now_time,FileName)
    return os.path.join('uploads/',NewFileName)

class Catogory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=GetFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    Catogory = models.ForeignKey(Catogory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=GetFileName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    Product_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    Trending = models.BooleanField(default=False,help_text='0-default,1-Trending')
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price
    

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address_line1}, {self.city}, {self.state}, {self.country}"
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return f"{self.user.first_name}, {self.product.name}, {self.created_at}`1"