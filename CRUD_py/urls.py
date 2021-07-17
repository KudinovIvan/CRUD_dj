from django.contrib import admin
from django.urls import path
from django.urls import re_path
from main import views

urlpatterns = [
    path('', views.index),
    path('app/', views.app),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('reset/', views.reset),
    path('red/', views.red),
    path('perm/', views.perm),
    path('admin/', admin.site.urls),
]
