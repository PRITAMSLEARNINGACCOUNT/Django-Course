from django.shortcuts import render


def Main_Function(request):
    return render(request, "Second_Webpage.html")
