from django.contrib import admin
from . models import Docente, Categoria, AnoLetivo, News,\
    AreaCientifica, Cadeira, Recurso, Turma, Nota


# Register your models here.
admin.site.register(Docente)