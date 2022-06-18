from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Tarjeta, ClienteTarjeta, Cliente
from .serializers import (UserSerializer, ClienteTarjetaSerializer, ClienteSerializer,
    TarjetaSerializer)

def index(request):
    """ Vista o función que atiende la url GET / """
    return render(request, "banco_app/index.html")

def acerca_de(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    return render(request, "banco_app/acerca-de.html")

def tarjetas(request):
    """ Vista o función que atiende la url GET /tarjetas/ """
    tarjetas_all = Tarjeta.objects.all()
    return render(request, "banco_app/tarjetas.html",
        {
            "tarjetas": tarjetas_all,
        }
    )

@login_required()
def portal(request):
    """ Vista o función que atiende la url GET /portal/ """
    user = request.user  # obtenemos el usuario activo
    tarjetas_usuario = ClienteTarjeta.objects.filter(cliente__user=user)
    return render(request, "banco_app/portal.html",
        {
            "tarjetas": tarjetas_usuario,
        }
    )


class UserViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla User con url /api/users
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los usuarios disponibles.
   queryset = User.objects.all().order_by('id')

   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = UserSerializer


class ClienteTarjetaViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla ClienteTarjeta con url
   /api/clientetarjeta
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre la tabla ClienteTarjeta
   queryset = ClienteTarjeta.objects.all().order_by('id')

   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = ClienteTarjetaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Cliente con url
   /api/cliente
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre la tabla ClienteTarjeta
   queryset = Cliente.objects.all().order_by('id')

   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = ClienteSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Tarjeta con url
   /api/tarjeta
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre la tabla ClienteTarjeta
   queryset = Tarjeta.objects.all().order_by('id')

   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = TarjetaSerializer

# def login_user(request):
#     """ Vista o función que atiende la url GET, POST /login/ """

#     # Si hay datos vía POST se procesan
#     if request.method == "POST":
#         # Se obtienen los datos del formulario
#         username = request.POST["username"]
#         password = request.POST["password"]
#         next = request.GET.get("next", "/")
#         acceso = authenticate(username=username, password=password)
#         if acceso != None:
#             # Se agregan datos al request para mantener activa la sesión
#             login(request, acceso)
#             # Y redireccionamos a next
#             return redirect(next)
#         else:
#             # Usuario malo
#             msg = "Datos incorrectos, intente de nuevo!"
#     else:
#         # Si no hay datos POST, se muestra el formulario por primera vez
#         msg = ""

#     return render(request, "banco_app/login.html", {"msg": msg})

# def logout_user(request):
#     """ Vista o función que atiende la url GET /logout/ """
#     logout(request)  # eliminamos las variables de sesión del usuario

#     return redirect("/")


