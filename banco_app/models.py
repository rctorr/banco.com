from django.db import models
from django.contrib.auth.models import User


# Django ya cuenta con una tabla de Usuario llamada User
# class User(models.Model):
#     username = models.CharField(max_length=80)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     group = models.ForeignKey(Group)
#     email = models.EmailField()


class Cliente(models.Model):
    """ Define la tabla Cliente """
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),  # <- opcion
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)  # VARCHAR(1)
    TIPO = [
        ("PF", "Persona Física"),
        ("PM", "Persona Moral"),
    ]
    tipo = models.CharField(max_length=2, choices=TIPO, null=True, blank=True)  # VARCHAR(2)

    def __str__(self):
        for opcion in self.GENERO:
            if opcion[0] == self.genero:
                return opcion[1]


class Tarjeta(models.Model):
    """ Define la tabla Tarjeta """
    nombre = models.CharField(max_length=145)
    descripcion = models.CharField(max_length=256)
    interes = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre


class ClienteTarjeta(models.Model):
    """ Define la tabla Cliente Tarjeta """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    numeroTarjeta = models.IntegerField()
    creditoMax = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.numeroTarjeta)





