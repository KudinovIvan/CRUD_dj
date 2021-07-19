from django.contrib import admin
from django.urls import path
from django.urls import re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('admin/', admin.site.urls),
    path('signin/response-city/', views.player, name='response-city'),
]
