from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core import serializers
from django.forms.models import model_to_dict
import json

from .models import Docente, Categoria, AnoLetivo, AreaCientifica,\
    Cadeira, News, Recurso, Turma, Nota, Calendario
from .serializers import NewsSerializer, RecursoSerializer, NotaSerializer, CalendarioSerializer

from rest_framework.pagination import PageNumberPagination
from lei.pagination import NewsPageNumberPagination, CalendarioPageNumberPagination, RecursoPageNumberPagination
# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls = {
        # listar
        'List News': '/news-list',
        'List Recurso': '/recursos-list',
        'List RecursoAll': '/allrecursos-list',
        'List Notas': '/notas-list',
        'List Lei': '/lei-list',
        'List calendario': '/calendario-list',

        # recurso especifico

        'Detail Recuso': '/recursos-detail/<str:pk>/',

    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def newsList(request):

    news = News.objects.all().order_by('-id')
    paginator = NewsPageNumberPagination()
    news_result = paginator.paginate_queryset(news, request)
    serializer = NewsSerializer(news_result, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def recursoList(request):
    recursos = Recurso.objects.select_related('cadeira', 'docente', 'categoria', 'anoletivo').all().order_by('-id')
    paginator = RecursoPageNumberPagination()
    recurso_result = paginator.paginate_queryset(recursos, request)
    serializer = RecursoSerializer(recurso_result, many=True)
    return paginator.get_paginated_response(serializer.data)


# retornar os recursos não paginados
@api_view(['GET'])
def allrecursoList(request):
    recurso = Recurso.objects.select_related('cadeira', 'docente', 'categoria', 'anoletivo').all().order_by('-id')
    serializer = RecursoSerializer(recurso, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoDetail(request, pk):
    recurso = Recurso.objects.get(id=pk)
    serializer = RecursoSerializer(recurso, many=False)
    # print('Recurso:: ',serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def notaList(request):
    notas = Nota.objects.select_related('turma').all().order_by('-id')

    # dicionario para agrupar as notas por turma
    dicionario = {}
    print(notas)

    for nota in notas:
        # print(nota)
        # print(type(nota))
        if not nota.turma.turma in dicionario:
            dicionario[nota.turma.turma] = []
        #serializar as notas
        notaserialized = NotaSerializer(nota, many=False)
        dicionario[nota.turma.turma].append(notaserialized.data)
    # print(dicionario)

    serializer = NotaSerializer(notas, many=True)
    return Response(dicionario)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def calendarioList(request):

    calendario = Calendario.objects.all().order_by('dataInicio')
    serializer = CalendarioSerializer(calendario, many=True)
    return Response(serializer.data)


