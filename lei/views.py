from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoList(request):
    recursos = Recurso.objects.all()
    serializer = NewsSerializer(recursos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recursoDetail(request, pk):
    recursos = Recurso.objects.get(id=pk)
    serializer = RecursoSerializer(recursos, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def notaList(request):
    nota = Nota.objects.all()
    serializer = NotaSerializer(nota, many=True)
    return Response(serializer.data)
