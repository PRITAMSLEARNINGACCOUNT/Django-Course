from django.http import HttpResponse
from django.shortcuts import render


def html_showing(request):
    params = {"Final_function": "So finally we have done using templates in our django programme and also we have shown it in our website which is made by django."}
    return render(request, "for_templates.html",params)
