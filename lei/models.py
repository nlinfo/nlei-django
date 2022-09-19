from django.db import models
from django.utils import timezone
from django.conf import settings
import os

# Create your models here.


class Docente(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    numeroDeTelefone = models.PositiveIntegerField(blank=True, default='+239')

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class AnoLetivo(models.Model):
    data = models.CharField(max_length=12)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.data


class News(models.Model):
    cabecalho = models.CharField(max_length=250)
    corpo = models.TextField()
    imagem = models.ImageField(blank=True, null=True, upload_to='imagens/news')
    imagelink = models.URLField(blank=True)
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
    docente = models.ForeignKey(Docente, on_delete=models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    anoletivo = models.ForeignKey(AnoLetivo, on_delete=models.DO_NOTHING)

    ficheiro = models.FileField(null=True, upload_to='recurso/')
    link = models.URLField(blank=True)
    detalhe = models.TextField()
    data = models.DateTimeField(default=timezone.now)

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
    ficheiro = models.FileField(null=True, upload_to='nota/')

    def __str__(self):
        return self.titulo


# alunos

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    dataDeNascimento = models.DateField(default=timezone.now, blank=True, verbose_name='data de nascimento')
    numeroDeTelefone = models.PositiveIntegerField(blank=True, null=True, default='00239', verbose_name='numero de telefone')
    email = models.EmailField(null=True)

    def __str__(self):
        return self.nome


# calendário
class Calendario(models.Model):
    titulo = models.CharField(max_length=200)
    dataInicio = models.DateTimeField(default=timezone.now, verbose_name= 'data de inicio')
    dataFim = models.DateTimeField(default=timezone.now, verbose_name='data de fim')
    detalhe = models.TextField()

    def __str__(self):
        return self.titulo
