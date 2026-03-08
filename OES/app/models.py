from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=20,null=True,blank=False)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    P_ID=models.CharField(max_length=20,null=True,blank=False)
    P_Name=models.CharField(max_length=80,null=True,blank=False)
    P_Amount=models.CharField(max_length=20,null=True,blank=False)
    p_Image=models.ImageField(upload_to='product_image',null=True,blank=False)
    P_Info=models.TextField(max_length=120)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.P_Name)
    
class Cart(models.Model):
    User_ID=models.CharField(max_length=20,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


class Orders(models.Model):
    TID=models.CharField(max_length=20,null=True,blank=False)
    User_ID=models.CharField(max_length=20,null=True,blank=False)
    P_Name=models.CharField(max_length=20,null=True,blank=False)
    P_Amount=models.CharField(max_length=20,null=True,blank=False)
    P_Image=models.ImageField(upload_to='orderd_image',null=True,blank=False)
    Date_Time=models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return str(self.TID)   
    
class User_Detail(models.Model):
    UID=models.CharField(max_length=20,null=True,blank=False)
    U_Name=models.CharField(max_length=50,null=True,blank=False)
    U_Password=models.CharField(max_length=20,null=True,blank=False)
    U_Image=models.ImageField(default='user_details',null=True,blank=False)
    U_Email=models.CharField(max_length=120,null=True,blank=False)
    U_PoneNumber=models.CharField(max_length=20,null=True,blank=False)

    def __str__(self):
        return str(self.UID)


class ProductRating(models.Model):
    User_ID=models.CharField(max_length=20,null=False,blank=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='ratings')
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review=models.TextField(max_length=300,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("User_ID", "product")

    def __str__(self):
        return f"{self.product.P_Name} - {self.rating}"



