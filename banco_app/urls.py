from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de/', views.acerca_de, name="acerca_de"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('portal/', views.portal, name="portal"),

    path('login/', auth_views.LoginView.as_view(
        template_name="banco_app/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
