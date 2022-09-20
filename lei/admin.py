from pyexpat import model
from django.contrib import admin
from .models import Docente, Categoria, AnoLetivo, News, \
    AreaCientifica, Cadeira, Recurso, Turma, Nota, Aluno, Calendario
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django_summernote.admin import SummernoteModelAdmin
from pathlib import Path
import os
# Import mimetypes module
import mimetypes  # um dos pacotes para baixar ficheiros
# Import HttpResponse module (para baixar file)
from django.http.response import HttpResponse
from django.core.files.storage import default_storage


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
    # summernote_fields = ('corpo',)


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

@admin.action(description='Baixar lista de email ')
def dowload_email_list(modeladmin, request, queryset):
    alunos = Aluno.objects.all().order_by('nome')

    # dicionario para agrupar os alunos por turma
    dicionario = {}
    turmas = []

    for aluno in alunos:
        if not aluno.turma.turma in dicionario:
            dicionario[aluno.turma.turma] = []

        nome = str(aluno.nome)
        email = str(aluno.email)
        turma = str(aluno.turma)
        dados_aluno = f'{nome} - {email} - {turma}'
        dicionario[aluno.turma.turma].append(dados_aluno)
        turmas.append(aluno.turma.turma)
    # print(dicionario)
    turmas = set(turmas)
    nome_adicional = ''
    for turma in turmas:
        nome_adicional += turma

    BASE_DIR = Path(__file__).resolve().parent.parent
    caminho = os.path.join(BASE_DIR, 'static/images/aluno')
    nome_do_ficheiro = f'email_completo_turmas_{nome_adicional}.txt'

    # escrever no ficheiro
    with open(f'{caminho}/{nome_do_ficheiro}', 'w') as file:
        lista_email = ''

        file.write(f'Nome  -  Email - Turma\n')
        for turma in queryset:
            # print(dicionario[turma.turma])
            index = 1
            file.write(f'\n\nTurma:  {str(turma)}\n')
            for aluno in dicionario[turma.turma]:
                file.write(f'{index}. {aluno}\n')
                index += 1

                # pegar o email do aluno pela string
                email = aluno.split('-')
                lista_email += email[1]

        file.write(f'\n\nLista com todos os emails:\n {lista_email}\n')

    # Open the file for reading content
    filepath = f'{caminho}/{nome_do_ficheiro}'
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % nome_do_ficheiro
    # Return the response value
    return response


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'sala')
    list_per_page = 50
    actions = [dowload_email_list]


# nota
@admin.action(description='Enviar email aos alunos')
def send_email(modeladmin, request, queryset):
    nota = queryset

    titulo = nota.values('titulo')[0]['titulo']
    id_turma_query = nota.values('turma_id')
    id_turma = id_turma_query[0]['turma_id']

    turmamodel = Turma.objects.get(id=id_turma)

    # print(nota.values(), 'id:', id_turma)
    # print('modeladmin', titulo)

    # importar alunos
    alunos = Aluno.objects.filter(turma_id=id_turma).values()
    lista_alunos = []
    lista_email_alunos = []

    for aluno in alunos:
        lista_alunos.append([aluno['nome'], aluno['email']])
        lista_email_alunos.append(aluno['email'])

    # enviar email
    # print(lista_email_alunos)
    template = render_to_string('frontend/email_template.html', {'turma': turmamodel, 'nota': titulo})
    email = EmailMessage(
        'Aviso de publicação de nota!',
        template,
        settings.EMAIL_HOST_USER,
        lista_email_alunos
    )
    email.content_subtype = "html"
    email.fail_silently = False
    email.send()


class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'turma')
    list_per_page = 50
    actions = [send_email]


# aluno

@admin.action(description='Baixar lista de email completo')
def dowload_fullemail_list(modeladmin, request, queryset):
    alunos = Aluno.objects.all().order_by('nome')

    BASE_DIR = Path(__file__).resolve().parent.parent
    caminho = os.path.join(BASE_DIR, 'static/images/aluno')
    nome_do_ficheiro = 'email_completo.txt'

    with open(f'{caminho}/{nome_do_ficheiro}', 'w') as file:
        lista_email = ''
        index = 1
        file.write(f'Nome  -  Email - Turma\n\n')
        for aluno in alunos:
            nome = aluno.nome
            email = aluno.email
            turma = aluno.turma.turma
            lista_email += f' {email} '
            file.write(f'{index}. {nome} - {email} - {turma}\n')
            index += 1

        file.write(f'\n\nLista com todos os emails:\n {lista_email}\n')

    # Open the file for reading content
    filepath = f'{caminho}/{nome_do_ficheiro}'
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % nome_do_ficheiro
    # Return the response value
    return response


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numeroDeTelefone', 'turma')
    list_per_page = 50
    list_editable = ('email', 'numeroDeTelefone')
    actions = [dowload_fullemail_list]


# calendário
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataInicio', 'dataFim')
    list_per_page = 50
    # summernote_fields = ('detalhe',)


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
