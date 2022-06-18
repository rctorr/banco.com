from rest_framework import serializers

from django.contrib.auth.models import User

from .models import ClienteTarjeta, Cliente, Tarjeta

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para el modelo User """
    class Meta:
        # Se define sobre que modelo actua
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ClienteTarjetaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para ClienteTarjeta """
    class Meta:
        # Se define sobre que modelo actúa
        model = ClienteTarjeta
        # Se definen los campos a incluir
        fields = ('id', 'cliente', 'tarjeta', 'numeroTarjeta', 'creditoMax')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Cliente """
    class Meta:
        # Se define sobre que modelo actúa
        model = Cliente
        # Se definen los campos a incluir
        fields = ('id', 'user', 'fechaNacimiento', 'genero', 'tipo')


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tajreta """
    class Meta:
        # Se define sobre que modelo actúa
        model = Tarjeta
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'descripcion', 'interes')


