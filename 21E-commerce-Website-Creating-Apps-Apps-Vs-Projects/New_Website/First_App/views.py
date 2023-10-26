from django.shortcuts import render
from django.http import HttpResponse


def function_1(request):
    return HttpResponse("This is from the first app")
