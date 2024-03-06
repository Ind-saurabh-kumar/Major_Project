from django.db import models

# Create your models here.

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    desc =models.TextField(max_length=500)
    pnumber=models.IntegerField(max_length=10)


    def __str__(self):
        return self.name 
    
    


    

