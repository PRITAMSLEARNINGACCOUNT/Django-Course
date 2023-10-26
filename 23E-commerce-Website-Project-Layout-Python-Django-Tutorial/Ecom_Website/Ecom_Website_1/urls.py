from django.urls import path
from . import Ecomerce_Website

urlpatterns = [
    path("/Ecom_Website_1", Ecomerce_Website.index,
         name="This is just a function for laying out the pipeline of our website"),
    path("/Customer Care", Ecomerce_Website.Customer_Care,
         name="This is also just a function for laying the pipeline"),
    path("/About us", Ecomerce_Website.About_Us,
         name="This is also just a function for laying the pipeline"),
    path("/Error", Ecomerce_Website.Error,
         name="This is also just a function for laying the pipeline"),
    path("/Trace Product", Ecomerce_Website.Tracking_Product,
         name="This is also just a function for laying the pipeline"),
]
