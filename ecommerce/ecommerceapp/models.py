from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    desc =models.TextField(max_length=500)
    pnumber=models.IntegerField(max_length=10)


    def __str__(self):
        return self.name 
    




class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default=" ")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500) 

    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.product_name
    
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length = 5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField(max_length=100)
    oid = models.CharField(max_length= 50, blank = True)
    amountpaid = models.CharField(blank = True, null= True, max_length=500)
    paymentstatus= models.CharField(max_length = 50, blank= True)
    phone = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name, self.order_id
    



class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key= True)
    order_id = models.IntegerField(default= 0)
    update_desc = models.CharField(max_length=5000)
    delivered = models.BooleanField(default= False)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] +"....."






    

