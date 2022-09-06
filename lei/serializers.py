from rest_framework import serializers
from lei import pagination
from .models import Docente, Categoria, AnoLetivo, AreaCientifica,\
    Cadeira, News, Recurso, Turma, Nota, Calendario


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class AnoLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = '__all__'


class AreaCientificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCientifica
        fields = '__all__'


class CadeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadeira
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class RecursoSerializer(serializers.ModelSerializer):

    cadeira = CadeiraSerializer()
    docente = DocenteSerializer()
    categoria = CategoriaSerializer()
    anoletivo = AnoLetivoSerializer()

    class Meta:
        model = Recurso
        fields = '__all__'


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer()

    class Meta:
        model = Nota
        fields = '__all__'


class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'
