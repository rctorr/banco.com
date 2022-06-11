from django.contrib import admin
from .models import Cliente, Tarjeta, ClienteTarjeta

class ClienteAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "user", "fechaNacimiento", "genero", "tipo")


class TarjetaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("nombre", "descripcion", "interes")


class ClienteTarjetaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("numeroTarjeta", "cliente", "tarjeta", "creditoMax")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(ClienteTarjeta, ClienteTarjetaAdmin)



