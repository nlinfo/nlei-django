from django.contrib import admin
from . models import Docente, Categoria, AnoLetivo, News,\
    AreaCientifica, Cadeira, Recurso, Turma, Nota


# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome')


class AnoLetivoAdmin(admin.ModelAdmin):
    list_display = ('data', 'observacao')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'data', 'informacao')


class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome')


class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'areacientifica', 'tipo')


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'anoletivo')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'sala')


class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'turma')
    

admin.site.register(Docente, DocenteAdmin)

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(AnoLetivo, AnoLetivoAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(AreaCientifica, AreaCientificaAdmin)

admin.site.register(Cadeira, CadeiraAdmin)

admin.site.register(Recurso, RecursoAdmin)

admin.site.register(Turma, TurmaAdmin)

admin.site.register(Nota, NotaAdmin)

