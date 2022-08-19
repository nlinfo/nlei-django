from django.db import models
from django.utils import timezone

# Create your models here.


class Docente(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(blank=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)


class AnoLetivo(models.Model):
    data = models.IntegerField()
    observacao = models.TextField(blank=True)


class News(models.Model):
    cabecalho = models.TextField()
    corpo = models.TextField()
    #introduzir imagem
    imagelink = models.URLField()
    data = models.DateTimeField(default=timezone.now)
    informacao = models.BooleanField(default=False)


class AreaCientifica(models.Model):
    nome = models.CharField(max_length=50)


class Cadeira(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=50)
    areacientifica = models.ForeignKey(AreaCientifica, on_delete=models.DO_NOTHING)
    tipo = models.IntegerField(blank=True)


class Recurso(models.Model):
    nome = models.CharField(max_length=250)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.DO_NOTHING)
    docente = models.ForeignKey(Docente, on_delete=models.DO_NOTHING, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    anoletivo = models.ForeignKey(AnoLetivo, on_delete=models.DO_NOTHING)
    #introduzir o campo para ficheiro
    link = models.URLField(blank=True)
    detalhe = models.TextField()


class Turma(models.Model):
    turma = models.CharField(max_length=2)
    sala = models.IntegerField()


class Nota(models.Model):
    titulo = models.CharField(max_length=150)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    #introduzir campo para ficheiro
