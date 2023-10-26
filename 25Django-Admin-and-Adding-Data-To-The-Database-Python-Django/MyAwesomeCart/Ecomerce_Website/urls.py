from django.urls import path
from . import Website
urlpatterns = [
    path("/", Website.main, name="Displays The Home Page Of Our Ecomerce Website"),
    path("/Customer Care", Website.Customer_Care,
         name="This is also just a function for laying the pipeline"),
    path("/About us", Website.About_Us,
         name="This is also just a function for laying the pipeline"),
    path("/Error", Website.Error,
         name="This is also just a function for laying the pipeline"),
    path("/Trace Product", Website.Tracking_Product,
         name="This is also just a function for laying the pipeline"),

]
