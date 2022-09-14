from django.contrib import admin
from .models import Docente, Categoria, AnoLetivo, News, \
    AreaCientifica, Cadeira, Recurso, Turma, Nota, Aluno, Calendario
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings


# Register your models here.


# docente
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')
    list_per_page = 50


# categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 10


# ano letivo
class AnoLetivoAdmin(admin.ModelAdmin):
    list_display = ('data', 'observacao')
    list_display_links = ('data', 'observacao')
    list_per_page = 50


# news
class NewsAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'data', 'informacao')
    list_per_page = 50
    list_display_links = ('cabecalho', 'data')


# area cientifica
class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 50


# cadeira
class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'areacientifica', 'tipo')
    list_display_links = ('nome', 'sigla')
    list_per_page = 50


# recurso
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'anoletivo')
    list_display_links = ('nome', 'categoria')
    list_per_page = 50


# turma
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'sala')
    list_per_page = 50


# nota
@admin.action(description='Enviar email aos alunos')
def send_email(modeladmin, request, queryset):
    nota = queryset

    titulo = nota.values('titulo')[0]['titulo']
    id_turma_query = nota.values('turma_id')
    id_turma = id_turma_query[0]['turma_id']

    turmamodel = Turma.objects.get(id=id_turma)

    print(nota.values(), 'id:', id_turma)
    print('modeladmin', titulo)

    # importar alunos
    alunos = Aluno.objects.filter(turma_id=id_turma).values()
    print(alunos)
    lista_alunos = []
    lista_email_alunos = []
    print(lista_email_alunos)

    for aluno in alunos:
        # print(aluno['nome'], aluno['email'])
        print(aluno)
        lista_alunos.append([aluno['nome'], aluno['email']])
        lista_email_alunos.append(aluno['email'])

    # enviar email
    print(lista_email_alunos)
    template = render_to_string('frontend/email_template.html', {'turma': turmamodel, 'nota': titulo})
    email = EmailMessage(
        'Aviso de nota!',
        template,
        settings.EMAIL_HOST_USER,
        lista_email_alunos
    )
    email.fail_silently = False
    email.send()


class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'turma')
    list_per_page = 50
    actions = [send_email]


# aluno
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numeroDeTelefone', 'turma')
    list_per_page = 50
    list_editable = ('email', 'numeroDeTelefone')


# calendário
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataInicio', 'dataFim')
    list_per_page = 50


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

admin.site.register(Calendario, CalendarioAdmin)
