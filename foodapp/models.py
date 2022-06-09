from django.db import models

class Userdetails(models.Model):
        fname = models.CharField(max_length=256)
        lname  = models.CharField(max_length = 250)
        username = models.CharField(max_length=100)
        phone = models.CharField(max_length=20)
        email = models.CharField(max_length=25)
        address = models.CharField(max_length=255)
        password = models.CharField(max_length=255)
	
        class Meta:
            db_table="userinfo"
            
            
class Image(models.Model):  
    caption = models.CharField(max_length=200,default=None)
    price=models.CharField(max_length=100,default=None)  
    image = models.ImageField(upload_to='images',default=None)
    # dish_category = models.CharField(max_length=200, default="")
    
    class Meta:
        db_table="dishes"
        
class Order(models.Model):
    dish=models.CharField(max_length=254)
    username=models.CharField(max_length=254)
    phone=models.CharField(max_length=254)
    address=models.CharField(max_length=254)
    price=models.CharField(max_length=254)
    quantity=models.CharField(max_length=254)
    
    class Meta:
        db_table="orders"
     