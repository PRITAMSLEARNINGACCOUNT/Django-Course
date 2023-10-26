"""
URL configuration for practice_on_pipeline project.

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
from . import quick_quiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home_page', quick_quiz.Home_page, name="Home Page"),
    path('Defination', quick_quiz.defination, name="Defination of pipeline"),
    path('First Pipeline', quick_quiz.pipeline_1, name="First Pipeline"),
    path('Second Pipeline', quick_quiz.pipeline_2, name="Second Pipeline"),
    path('Third Pipeline', quick_quiz.pipeline_3, name="Third Pipeline"),
    path('Fourth Pipeline', quick_quiz.pipeline_4, name="Fourth Pipeline"),
    path('Fifth Pipeline', quick_quiz.pipeline_5, name="Fifth Pipeline"),
]
