from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'frontend/index.html')


def lei(request):
    return render(request, 'frontend/lei.html')


def news(request):
    return render(request, 'frontend/news.html')


def recursos(request):
    return render(request, 'frontend/recursos.html')


def calendario(request):
    return render(request, 'frontend/calendario.html')


def notas(request):
    return render(request, 'frontend/notas.html')
