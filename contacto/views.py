from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm
from cafeteria.settings import *


def contacto(request):
    contact_form = ContactoForm()

    if request.method == "POST":
        contact_form = ContactoForm(data=request.POST)
        if contact_form.is_valid():

            context = {
                'name' : request.POST.get('name', ''),
                'email' : request.POST.get('email', ''),
                'message' : request.POST.get('content', ''),
            }

            # Creamos el correo
            email = EmailMessage(
                subject = 'Cafeteria',
                body = context['message'],
                from_email = EMAIL_HOST_USER,
                to = ['gerardo.garcia@c3ntro.com'],
                #headers = {'reply-to':email}
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contacto')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contacto')+"?fail")
    
    return render(request, "contacto/contacto.html",{'form':contact_form})