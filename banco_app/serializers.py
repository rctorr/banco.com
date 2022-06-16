from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para el modelo User """
    class Meta:
        # Se define sobre que modelo actua
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

