# Generated by Django 5.1.2 on 2024-10-10 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil/')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('curso', 'Curso'), ('titulo', 'Titulo Universitario'), ('certificacion', 'Certificacion'), ('seminario', 'Seminario')], default='curso', max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='estudios/')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudios', to='App_Portafolio.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_realizacion', models.DateField()),
                ('url_proyecto', models.URLField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='proyectos/')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='App_Portafolio.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tecnologias/')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tecnologias', to='App_Portafolio.perfil')),
            ],
        ),
    ]