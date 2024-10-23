"""
URL configuration for Portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),


    path('registro/', UserRegisterView.as_view(), name='registro_usuario'),
    path('edit/', UserEditView.as_view(), name='edit_usuario'),
    path('edit-pass/', CambiarPassword.as_view(), name='edit_pass'),


    path('perfil/', PerfilDetailView.as_view(), name='perfil_detalle'),
    path('perfil/nuevo', PerfilCreateView.as_view(), name='perfil_crear'),
    path('perfil/editar', PerfilUpdateView.as_view(), name='perfil_editar'),
    path('perfil/eliminar', PerfilDeleteView.as_view(), name='perfil_borrar'),


    path('estudios/', EstudioListView.as_view(), name='estudio_lista'),
    path('estudios/<int:pk>/', EstudioDetailView.as_view(), name='estudio_detalle'),
    path('estudios/nuevo/', EstudioCreateView.as_view(), name='estudio_crear'),
    path('estudios/editar/<int:pk>/', EstudioUpdateView.as_view(), name='estudio_editar'),
    path('estudios/borrar/<int:pk>/', EstudioDeleteView.as_view(), name='estudio_borrar'),


    path('tecnologias/', TecnologiaListView.as_view(), name='tecnologia_lista'),
    path('tecnologias/<int:pk>/', TecnologiaDetailView.as_view(), name='tecnologia_detalle'),
    path('tecnologias/nuevo/', TecnologiaCreateView.as_view(), name='tecnologia_crear'),
    path('tecnologias/editar/<int:pk>/', TecnologiaUpdateView.as_view(), name='tecnologia_editar'),
    path('tecnologias/borrar/<int:pk>/', TecnologiaDeleteView.as_view(), name='tecnologia_borrar'),


    path('proyectos/', ProyectoListView.as_view(), name='proyecto_lista'),
    path('proyectos/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto_detalle'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto_crear'),
    path('proyectos/editar/<int:pk>/', ProyectoUpdateView.as_view(), name='proyecto_editar'),
    path('proyectos/borrar/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto_borrar'),


    path('home/', paginaPrincipal , name='Home'),


    path('portfolio/', CurriculumView.as_view(), name='portfolio'),


    path('contacto/', ContactoView.as_view(), name='contactanos'),
    path('contacto/exito/', ContactoExitoView.as_view(), name='contacto_exito'),
]
