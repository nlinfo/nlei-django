from django.db import models
from django.utils import timezone

# Create your models here.


class Docente(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class AnoLetivo(models.Model):
    data = models.IntegerField()
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.data


class News(models.Model):
    cabecalho = models.CharField(max_length=250)
    corpo = models.TextField()
    #introduzir imagem
    imagelink = models.URLField()
    data = models.DateTimeField(default=timezone.now)
    informacao = models.BooleanField(default=False)

    def __str__(self):
        return self.cabecalho


class AreaCientifica(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=50)
    areacientifica = models.ForeignKey(AreaCientifica, on_delete=models.DO_NOTHING)
    tipo = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    nome = models.CharField(max_length=250)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.DO_NOTHING)
    docente = models.ForeignKey(Docente, on_delete=models.DO_NOTHING, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    anoletivo = models.ForeignKey(AnoLetivo, on_delete=models.DO_NOTHING)
    #introduzir o campo para ficheiro
    link = models.URLField(blank=True)
    detalhe = models.TextField()

    def __str__(self):
        return self.nome


class Turma(models.Model):
    turma = models.CharField(max_length=2)
    sala = models.IntegerField()

    def __str__(self):
        return self.turma


class Nota(models.Model):
    titulo = models.CharField(max_length=150)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    #introduzir campo para ficheiro

    def __str__(self):
        return self.titulo
