from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer
import json 

@api_view(['GET'])  
def get_profissional(request):
    profissional = Profissional.objects.all()
    serializer = ProfissionalSerializer(profissional, many=True)
    return Response(serializer.data)


@api_view(['GET','POST', 'PUT', 'DELETE'])
def profissional_manage(request): 
    if request.method == 'GET':
        try:
            id_prof = request.GET.get('profissional') 
            if id_prof is not None:
                try:
                    profissional = Profissional.objects.get(pk=id_prof)
                    serializer = ProfissionalSerializer(profissional) 
                    return Response(serializer.data)
                except Profissional.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND) 
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Parâmetro 'profissional' é obrigatório."})
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Parâmetro 'profissional' inválido."})
                

@api_view(['GET'])  
def get_consulta(request):
    consulta = Consulta.objects.all()
    serializer = ConsultaSerializer(consulta, many=True)
    return Response(serializer.data)

