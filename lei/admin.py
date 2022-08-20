from django.contrib import admin
from . models import Docente, Categoria, AnoLetivo, News,\
    AreaCientifica, Cadeira, Recurso, Turma, Nota


# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')


class AnoLetivoAdmin(admin.ModelAdmin):
    list_display = ('data', 'observacao')
    list_display_links = ('data', 'observacao')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'data', 'informacao')
    list_display_links = ('cabecalho', 'data')


class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')


class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'areacientifica', 'tipo')
    list_display_links = ('nome', 'sigla')


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'anoletivo')
    list_display_links = ('nome', 'categoria')


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

