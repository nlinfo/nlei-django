from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.forms.models import model_to_dict
import json

from .models import Docente, Categoria, AnoLetivo, AreaCientifica,\
    Cadeira, News, Recurso, Turma, Nota, Calendario
from .serializers import NewsSerializer, RecursoSerializer, NotaSerializer, CalendarioSerializer

from rest_framework.pagination import PageNumberPagination
from lei.pagination import NewsPageNumberPagination
# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls = {
        # listar
        'List News': '/news-list',
        'List Recurso': '/recursos-list',
        'List Notas': '/notas-list',
        'List Lei': '/lei-list',
        'List calendario': '/calendario-list',

        # recurso especifico

        'Detail Recuso': '/recursos-detail/<str:pk>/',

    }
    return Response(api_urls)


@api_view(['GET'])
def newsList(request):
    news = News.objects.all().order_by('-id')
    serializer = NewsSerializer(news, many=True)
    pagination = NewsPageNumberPagination
    return Response(serializer.data)


@api_view(['GET'])
def recursoList(request):
    recursos = Recurso.objects.all().order_by('-id')
    serializer = RecursoSerializer(recursos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoDetail(request, pk):
    recurso = Recurso.objects.get(id=pk)
    serializer = RecursoSerializer(recurso, many=False)
    # print('Recurso:: ',serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def notaList(request):
    notas = Nota.objects.all().order_by('-id')

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
def calendarioList(request):
    calendario = Calendario.objects.all().order_by('dataInicio')
    serializer = CalendarioSerializer(calendario, many=True)
    pagination_class = PageNumberPagination
    return Response(serializer.data)


