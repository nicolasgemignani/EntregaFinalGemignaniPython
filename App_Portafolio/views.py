from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Perfil, Estudio, Tecnologia, Proyecto, Contacto
from .forms import EstudioForm, ProyectoForm, ContactoForm, PerfilForm

from django.views import View
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


# Create your views here.


""" HOME """
@login_required
def paginaPrincipal(req):
    perfil_existe = Perfil.objects.filter(user=req.user).exists() if req.user.is_authenticated else False
    return render(req, 'home.html', {'perfil_existe': perfil_existe})



""" CRUD USUARIO """
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('Login')

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_usuario.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in list(form.fields):
            if field not in ['username', 'email', 'first_name', 'last_name']:
                form.fields.pop(field)
        return form

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/edit_pass.html'
    success_url = reverse_lazy('Home')



""" CRUD PERFIL """
class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = 'perfil/perfil_detalle.html'

    def get_object(self, queryset=None):
        try:
            return Perfil.objects.get(user=self.request.user)
        except Perfil.DoesNotExist:
            return redirect('perfil_crear')

class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = Perfil
    template_name = 'perfil/perfil_crear.html'
    form_class = PerfilForm
    success_url = reverse_lazy('perfil_detalle')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, *args, **kwargs):
        if Perfil.objects.filter(user=self.request.user).exists():
            return redirect('perfil_detalle')
        return super().dispatch(*args, **kwargs)

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    template_name = 'perfil/perfil_editar.html'
    form_class = PerfilForm
    success_url = reverse_lazy('perfil_detalle')

    def get_object(self, queryset=None):
        return Perfil.objects.get(user=self.request.user)
    
class PerfilDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = 'perfil/perfil_borrar.html'
    success_url = reverse_lazy('Home')

    def get_object(self, queryset=None):
        return Perfil.objects.get(user=self.request.user)




""" CRUD ESTUDIOS """
class EstudioListView(LoginRequiredMixin, ListView):
    model = Estudio
    template_name = 'estudios/estudio_lista.html'
    context_object_name = 'estudios'

    def get_queryset(self):
        return Estudio.objects.filter(perfil=self.request.user.perfil)

class EstudioDetailView(LoginRequiredMixin, DetailView):
    model = Estudio
    template_name = 'estudios/estudio_detalle.html'

    def get_queryset(self):
        return Estudio.objects.filter(perfil=self.request.user.perfil)

class EstudioCreateView(LoginRequiredMixin, CreateView):
    model = Estudio
    template_name = 'estudios/estudio_crear.html'
    form_class = EstudioForm
    success_url = reverse_lazy('estudio_lista')

    def form_valid(self, form):
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)

class EstudioUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudio
    template_name = 'estudios/estudio_editar.html'
    form_class = EstudioForm
    success_url = reverse_lazy('estudio_lista')

    def get_queryset(self):
        return Estudio.objects.filter(perfil=self.request.user.perfil)

class EstudioDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudio
    template_name = 'estudios/estudio_borrar.html'
    success_url = reverse_lazy('estudio_lista')

    def get_queryset(self):
        return Estudio.objects.filter(perfil=self.request.user.perfil)




""" CRUD TECNOLOGIA """
class TecnologiaListView(LoginRequiredMixin, ListView):
    model = Tecnologia
    template_name = 'tecnologias/tecnologia_lista.html'
    context_object_name = 'tecnologias'

    def get_queryset(self):
        return Tecnologia.objects.filter(perfil=self.request.user.perfil)
    
class TecnologiaDetailView(LoginRequiredMixin, DetailView):
    model = Tecnologia
    template_name = 'tecnologias/tecnologia_detalle.html'

    def get_queryset(self):
        return Tecnologia.objects.filter(perfil=self.request.user.perfil)
    
class TecnologiaCreateView(LoginRequiredMixin, CreateView):
    model = Tecnologia
    template_name = 'tecnologias/tecnologia_crear.html'
    fields = ['nombre', 'imagen']
    success_url = reverse_lazy('tecnologia_lista')

    def form_valid(self, form):
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)
    
class TecnologiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tecnologia
    template_name = 'tecnologias/tecnologia_editar.html'
    fields = ['nombre', 'imagen']
    success_url = reverse_lazy('tecnologia_lista')

    def get_queryset(self):
        return Tecnologia.objects.filter(perfil=self.request.user.perfil)
    
class TecnologiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tecnologia
    template_name = 'tecnologias/tecnologia_borrar.html'
    success_url = reverse_lazy('tecnologia_lista')

    def get_queryset(self):
        return Tecnologia.objects.filter(perfil=self.request.user.perfil)
    


""" CRUD PROYECTO """
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyectos/proyecto_lista.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(perfil=self.request.user.perfil)

class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'proyectos/proyecto_detalle.html'

    def get_queryset(self):
        return Proyecto.objects.filter(perfil=self.request.user.perfil)

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = 'proyectos/proyecto_crear.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_lista')

    def form_valid(self, form):
        form.instance.perfil = self.request.user.perfil
        return super().form_valid(form)

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'proyectos/proyecto_editar.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyecto_lista')

    def get_queryset(self):
        return Proyecto.objects.filter(perfil=self.request.user.perfil)

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'proyectos/proyecto_borrar.html'
    success_url = reverse_lazy('proyecto_lista')

    def get_queryset(self):
        return Proyecto.objects.filter(perfil=self.request.user.perfil)
    


""" CURRICULUM """
class CurriculumView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = Perfil.objects.get(user=self.request.user)
        context['perfil'] = perfil
        context['estudios'] = perfil.estudios.all()
        context['tecnologias'] = perfil.tecnologias.all()
        context['proyectos'] = perfil.proyectos.all()
        return context
    

""" CONTACTANOS """
class ContactoView(View):
    def get(self, request):
        form = ContactoForm()
        return render(request, 'contacto/contacto.html', {'form': form})

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guarda el contacto en la base de datos
            contacto = Contacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            subject = 'Nuevo mensaje de contacto'
            message = f'Nombre: {contacto.nombre}\nEmail: {contacto.email}\nMensaje: {contacto.mensaje}'
            mail = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails='nicolasgemignani@outlook.com', 
                subject=subject,
                html_content=message
            )

            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(mail)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                return render(request, 'contacto/contacto_exito.html')
            except Exception as e:
                print(str(e))
                return HttpResponse('Hubo un error al enviar el correo, inténtalo de nuevo.')

        return render(request, 'contacto/contacto.html', {'form': form})
    
class ContactoExitoView(TemplateView):
    template_name = 'contacto/contacto_exito.html'