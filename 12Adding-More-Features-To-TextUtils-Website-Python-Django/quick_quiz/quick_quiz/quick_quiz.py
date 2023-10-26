from django.http import HttpResponse
from django.shortcuts import render


def main_website(request):
    return render(request, "Website.html")


def analyze(request):
    user_text = request.GET.get("User_text")
    # length = len(user_text)
    length = 0
    for a in user_text:
        length += 1
    parameters = {"length": length}
    return render(request, "Analyzed_text.html", parameters)
