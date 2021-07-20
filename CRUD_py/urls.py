from django.contrib import admin
from django.urls import path
from django.urls import re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('cities/', views.cities),
    path('detect/', views.detect),
    path('signup/', views.signup),
    path('admin/', admin.site.urls),
    path('cities/response-city/', views.player, name='response-city'),
]
