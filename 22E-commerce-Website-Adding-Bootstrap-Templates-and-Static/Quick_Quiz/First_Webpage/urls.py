from django.urls import path
from . import First_Webpage
urlpatterns = [
    path("", First_Webpage.Main,
         name="This is the first webpage"),

]
