from django.http import HttpResponse
from django.shortcuts import render


def main_website(request):
    return render(request, "Website.html")


def Space_Remover(request):
    user_text = request.GET.get("User_text")
    Empty_string = ""
    for a in user_text:
        if a == " ":
            pass
        else:
            Empty_string += a

    parameters = {"Analyzed_text": Empty_string}
    return render(request, "Analyzed_text.html", parameters)
