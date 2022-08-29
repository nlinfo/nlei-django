from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.forms.models import model_to_dict
import json

from .models import Docente, Categoria, AnoLetivo, AreaCientifica,\
    Cadeira, News, Recurso, Turma, Nota
from .serializers import NewsSerializer, RecursoSerializer, NotaSerializer

# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls = {
        # listar
        'List News': '/news-list',
        'List Recurso': '/recursos-list',
        'List Notas': '/notas-list',
        'List Lei': '/lei-list',

        # recurso especifico

        'Detail Recuso': '/recursos-detail/<str:pk>/',

    }
    return Response(api_urls)


@api_view(['GET'])
def newsList(request):
    news = News.objects.all().order_by('-id')
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoList(request):
    recursos = Recurso.objects.all().order_by('-id')
    serializer = RecursoSerializer(recursos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoDetail(request, pk):
    recursos = Recurso.objects.get(id=pk)
    serializer = RecursoSerializer(recursos, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def notaList(request):
    notas = Nota.objects.all().order_by('-id')

    dicionario = {}
    print(notas)

    for nota in notas:
        print(nota)
        if not nota.turma.turma in dicionario:
            dicionario[nota.turma.turma] = []
        dicionario[nota.turma.turma].append(nota)
    print(dicionario)

    serializer = NotaSerializer(notas, many=True)
    return Response(serializer.data)
