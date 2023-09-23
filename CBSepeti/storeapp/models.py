from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
    Category_Name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return f"Name: {self.Category_Name}"

class Customers(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    E_Mail = models.EmailField()
      
    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customers.objects.get(E_Mail=email)
        except:
            return False
  
    def isExists(self):
        if Customers.objects.filter(E_Mail=self.E_Mail):
            return True
        return False
    
class Products(models.Model):
    Product_Name = models.CharField(max_length=60)
    Product_Price = models.IntegerField(default=0)
    Category_ID = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Product_Description = models.CharField(max_length=250, default='', blank=True, null=True)
    Product_Image = models.ImageField(upload_to='uploads/products/')
  
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(Category_ID=category_id)
        else:
            return Products.get_all_products()

class Orders(models.Model):
    Product_ID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Customer_Name = models.CharField(max_length=50, default="Test")
    Quantity = models.IntegerField(default=1)
    Price = models.IntegerField()
    Date = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(default="False")
  
    def placeOrder(self):
        self.save()
  