from rest_framework import serializers
from .models import Profissional, Consulta

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Consulta
        fields = '__all__'
