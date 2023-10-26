"""
URL configuration for My_Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Final_Website_Rebuild
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Final_Website_Rebuild.Webpage_Show,
         name="This function shows the main webpage"),
    path("Main_Function", Final_Website_Rebuild.main,
         name="This function decides what to do or not to do"),
    path("Contact_Us", Final_Website_Rebuild.Contact_us,
         name="This pipeline shows the webpage of contact us"),
    path("About_Us", Final_Website_Rebuild.About_Us,
         name="This pipeline shows the webpage of about us"),
]
