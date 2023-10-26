from django.urls import path
from . import Second_Webpage
urlpatterns = [
    path("", Second_Webpage.Main_Function,
         name="This is the first webpage"),

]
