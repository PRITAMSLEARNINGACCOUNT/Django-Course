from django.urls import path
from . import Ecomerce_Website
urlpatterns = [
    path("/Ecom_Website_2", Ecomerce_Website.index,
         name="This is also just a function for laying the pipeline"),
    path("/Customer Care", Ecomerce_Website.Customer_Care,
         name="This is also just a function for laying the pipeline"),
    path("/About us", Ecomerce_Website.About_Us,
         name="This is also just a function for laying the pipeline"),
    path("/Product View", Ecomerce_Website.Product_View,
         name="This is also just a function for laying the pipeline"),
    path("/Trace Product", Ecomerce_Website.Tracking_Product,
         name="This is also just a function for laying the pipeline"),


]
