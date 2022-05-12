from django.contrib import admin
from django.urls import path
from . import views

app_name = "demoapp"
urlpatterns = [
    path('',views.index,name = "index"),
    path('register',views.register,name = "register"),
    path('sample',views.sample,name = "sample"),


]
