from django.db import models


class Product_Details(models.Model):
    Product_ID = models.AutoField
    Product_Name = models.CharField(max_length=100)
    Product_Description = models.CharField(max_length=500)
    Product_Price = models.IntegerField()
    Product_Image = models.ImageField()

    def __str__(self):
        return self.Product_Name
