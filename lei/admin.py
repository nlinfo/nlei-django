from django.contrib import admin
from . models import Docente, Categoria, AnoLetivo, News,\
    AreaCientifica, Cadeira, Recurso, Turma, Nota, Aluno


# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')
    list_per_page = 50



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 10


class AnoLetivoAdmin(admin.ModelAdmin):
    list_display = ('data', 'observacao')
    list_display_links = ('data', 'observacao')
    list_per_page = 50


class NewsAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'data', 'informacao')
    list_per_page = 50
    list_display_links = ('cabecalho', 'data')


class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 50


class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'areacientifica', 'tipo')
    list_display_links = ('nome', 'sigla')
    list_per_page = 50


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'anoletivo')
    list_display_links = ('nome', 'categoria')
    list_per_page = 50


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'sala')
    list_per_page = 50


class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'turma')
    list_per_page = 50


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numeroDeTelefone', 'turma')
    list_per_page = 50
    list_editable = ('email', 'numeroDeTelefone')


admin.site.register(Docente, DocenteAdmin)

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(AnoLetivo, AnoLetivoAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(AreaCientifica, AreaCientificaAdmin)

admin.site.register(Cadeira, CadeiraAdmin)

admin.site.register(Recurso, RecursoAdmin)

admin.site.register(Turma, TurmaAdmin)

admin.site.register(Nota, NotaAdmin)

admin.site.register(Aluno, AlunoAdmin)

