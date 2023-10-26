from django.shortcuts import render
from .models import Products_Detail


def main(request):
    data = Products_Detail.objects.all()
    params = {
      
    }
    for i in range(len(data)):
        params.__setitem__(f"Product_{i+1}", data[i])
    return render(request, "Main_Website.html", params)


def Customer_Care(request):
    return render(request, "Contact_Us.html")


def About_Us(request):
    return render(request, "About_Us.html")


def Tracking_Product(request):
    return render(request, "Trace_Product.html")


def Error(request):
    Tracking_Id = request.POST.get("Text_Entry")
    if Tracking_Id == "":
        return render(request, "Error_1.html")
    else:
        return render(request, "Error_2.html")
