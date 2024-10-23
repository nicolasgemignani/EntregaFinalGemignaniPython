from django.core.mail import send_mail
from django.conf import settings

def enviar_correo(contacto):
    subject = 'Nuevo mensaje de contacto'
    message = f'Nombre: {contacto["nombre"]}\nEmail: {contacto["email"]}\nMensaje: {contacto["mensaje"]}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['nicolasgemignani@outlook.com']  

    send_mail(subject, message, from_email, recipient_list)
