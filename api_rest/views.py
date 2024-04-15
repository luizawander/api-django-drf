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
                
                
    if request.method =='POST':        
        new_profissional = request.data
        serializer = ProfissionalSerializer(data=new_profissional)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)     
     

    if request.method =='PUT': 
        id_prof = request.data.get('id_prof')
        try:
            update_prof = Profissional.objects.get(pk=id_prof)
        except:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfissionalSerializer(update_prof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
                



@api_view(['GET'])  
def get_consulta(request):
    consulta = Consulta.objects.all()
    serializer = ConsultaSerializer(consulta, many=True)
    return Response(serializer.data)


@api_view(['GET','POST', 'PUT', 'DELETE'])    
def consulta_manage(request):
    
    if request.method == 'GET':
        try: 
            id_consulta = request.GET.get('consulta')
            if id_consulta is not None:
                try:
                    consulta = Consulta.objects.get(pk=id_consulta)
                    serializer = ConsultaSerializer(consulta) 
                    return Response (serializer.data)
                except Consulta.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Parâmetro 'consulta' é obrigatório."})
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Parâmetro 'consulta' inválido."})


    if request.method == 'PUT': 
        id_consulta = request.data.get('id_consulta')
        try:
            consulta = Consulta.objects.get(pk=id_consulta)
        except Consulta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ConsultaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    if request.method == 'POST':
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

