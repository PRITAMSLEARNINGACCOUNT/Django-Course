from django.urls import path
from . import views
urlpatterns = [
    path("",views.function_1,name="This is a fun programme")
]
