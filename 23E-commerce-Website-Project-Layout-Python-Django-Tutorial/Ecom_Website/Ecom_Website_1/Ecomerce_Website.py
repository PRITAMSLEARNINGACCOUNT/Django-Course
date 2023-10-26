from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "Ecom_Website.html")


def Customer_Care(request):
    return render(request, "Contact_Us.html")


def About_Us(request):
    return render(request, "About_Us.html")


def Tracking_Product(request):
    return render(request, "Trace_Product.html")


def Error(request):
    Tracking_Id = request.POST.get("Text_Entry")
    if Tracking_Id == "":
        return HttpResponse("You Didn't Enter Any Tracking Id To Track Please Give A Tracking Id")
    else:
        return HttpResponse("Sorry ever after you gave tracking id we can not able to trace it because the website is under devolopment")
