# Generated by Django 4.1 on 2022-08-19 18:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnoLetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField()),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('sigla', models.CharField(max_length=50)),
                ('tipo', models.IntegerField(blank=True)),
                ('areacientifica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lei.areacientifica')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabecalho', models.TextField()),
                ('corpo', models.TextField()),
                ('imagelink', models.URLField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('informacao', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=2)),
                ('sala', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('link', models.URLField(blank=True)),
                ('detalhe', models.TextField()),
                ('anoletivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lei.anoletivo')),
                ('cadeira', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lei.cadeira')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lei.categoria')),
                ('docente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lei.docente')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lei.turma')),
            ],
        ),
    ]
