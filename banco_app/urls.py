from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de/', views.acerca_de, name="acerca_de"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('login/', views.login_user, name="login"),
]
