from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'djangoApp'
urlpatterns = [
    path("index/", index, name='index'),
    path("details/", detail, name='detail'),
    path("header/", header, name='header'),
    path("footer/", footer, name='footer'),
]
