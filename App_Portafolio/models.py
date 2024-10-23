from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100)
    bio = models.TextField()
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre_completo
    

class Estudio(models.Model):

    TIPO_ESTUDIO = [
        ('curso', 'Curso'),
        ('titulo', 'Titulo Universitario'),
        ('certificacion', 'Certificacion'),
        ('seminario', 'Seminario')
    ]
    tipo = models.CharField(max_length=15, choices=TIPO_ESTUDIO, default='curso')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='estudios/', null=True, blank=True)
    perfil = models.ForeignKey(Perfil, related_name='estudios', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Tecnologia(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    perfil = models.ForeignKey(Perfil, related_name='tecnologias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Proyecto(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_realizacion = models.DateField()
    url_proyecto = models.URLField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    perfil = models.ForeignKey(Perfil, related_name='proyectos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre