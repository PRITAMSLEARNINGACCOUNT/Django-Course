from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Fucking World")
def Customer_Care(request):
    return HttpResponse("Customer Care page")
def About_Us(request):
    return HttpResponse("About Us page")
def Tracking_Product(request):
    return HttpResponse("Tracking Product page")
def Product_View(request):
    return HttpResponse("Product View page")
