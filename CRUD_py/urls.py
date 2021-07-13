from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('app/', views.app),
    path('auth/<int:id>/<str:name>/', views.auth),
    path('red/', views.red),
    path('perm/', views.perm),
    path('admin/', admin.site.urls),
]
