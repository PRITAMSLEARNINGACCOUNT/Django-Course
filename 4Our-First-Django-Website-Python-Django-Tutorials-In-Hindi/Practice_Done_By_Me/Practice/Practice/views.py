from django.http import HttpResponse


def testing(request):
    return HttpResponse("Hello fucking world")
