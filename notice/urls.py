from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="posts"),
    path('notice_about/', views.about, name ="about"),
    path('notice_web01/', views.web01, name="web01"),
    path('notice_web02/', views.web02, name="web02"),
]
