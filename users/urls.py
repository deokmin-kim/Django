from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.sign_in, name ="login"),
    path('logout/', views.sign_out, name ="logout"),
    path('register/', views.sign_up, name="register"),
    # path('post/edit/<int:id>', views.edit_post, name="post-edit"),
    # path('post/delete/<int:id>', views.delete_post, name="post-delete"),
    #
    # path('about/', views.about, name ="about"),
    # path('web01/', views.web01, name="web01"),
    # path('web02/', views.web02, name="web02"),

]
