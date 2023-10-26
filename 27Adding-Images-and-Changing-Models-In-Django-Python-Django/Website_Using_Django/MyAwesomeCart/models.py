from django.db import models


class Product_Details(models.Model):
    Product_Id = models.AutoField
    Product_Name = models.CharField(max_length=100)
    Product_Description = models.CharField(max_length=500)
    Product_Price = models.IntegerField()
    Product_Category = models.CharField(max_length=100)
    Product_Image = models.ImageField(upload_to='Media For The Website')

    def __str__(self):
        return self.Product_Name
