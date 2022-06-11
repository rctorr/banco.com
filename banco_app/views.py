from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Tarjeta

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

def login_user(request):
    """ Vista o función que atiende la url GET, POST /login/ """

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.GET.get("next", "/")
        acceso = authenticate(username=username, password=password)
        if acceso != None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST, se muestra el formulario por primera vez
        msg = ""

    return render(request, "banco_app/login.html", {"msg": msg})
