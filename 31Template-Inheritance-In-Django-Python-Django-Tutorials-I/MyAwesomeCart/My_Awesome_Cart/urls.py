from django.urls import path
from . import Website
urlpatterns = [
    path("/", Website.main, name="Displays The Home Page Of Our Ecomerce Website"),
    path("/Customer Care", Website.Customer_Care,
         name='Showing Information About Our Customer Care Service'),
    path("/About us", Website.About_Us,
         name="Showing About Our Website"),
    path("/Error", Website.Error,
         name="Showing Error Cause Site Is Under Devolopment"),
    path("/Trace Product", Website.Tracking_Product,
         name="Tracing Consumer's Product"),
]
