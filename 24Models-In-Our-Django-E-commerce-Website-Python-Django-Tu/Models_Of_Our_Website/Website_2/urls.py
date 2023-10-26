from django.urls import path
from . import views

urlpatterns = [
    path("/Ecom_Website_2", views.index,
         name="This is just a function for laying out the pipeline of our website"),
    path("/Customer Care", views.Customer_Care,
         name="This is also just a function for laying the pipeline"),
    path("/About us", views.About_Us,
         name="This is also just a function for laying the pipeline"),
    path("/Error", views.Error,
         name="This is also just a function for laying the pipeline"),
    path("/Trace Product", views.Tracking_Product,
         name="This is also just a function for laying the pipeline"),
]
