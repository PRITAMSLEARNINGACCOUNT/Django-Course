from django.db import models


class Products_Detail(models.Model):
    Product_ID = models.AutoField
    Product_Name = models.CharField(max_length=50)
    Product_Description = models.CharField(max_length=90)
    Product_Price = models.IntegerField()
    Product_Image = models.ImageField()

    def __str__(self):
        return self.Product_Name
