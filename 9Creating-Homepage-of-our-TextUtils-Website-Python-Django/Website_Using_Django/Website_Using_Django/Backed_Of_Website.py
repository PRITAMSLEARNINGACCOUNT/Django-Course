from django.http import HttpResponse
from django.shortcuts import render
# varriable = ''


def Website_Show(request):

    return render(request, "Website.html")


def analyze(request):

    return HttpResponse(f"This is the text given by the user --> {request.GET.get('This is a textarea')}")
