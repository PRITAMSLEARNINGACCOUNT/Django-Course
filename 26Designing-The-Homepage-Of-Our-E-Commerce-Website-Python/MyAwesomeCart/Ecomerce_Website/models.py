from django.db import models


class Product_Details(models.Model):
    Product_Name = models.CharField(max_length=100)
    Product_Id = models.AutoField
    Product_Price = models.IntegerField()
    Product_Description = models.CharField(max_length=500)
