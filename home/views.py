from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .models import Contact


def index(request):
    return render(request, 'index.html', {'data': 'This is index'})


def about(request):
    return render(request, 'about.html', {'data': 'This is about'})


def projects(request):
    return render(request, 'projects.html', {'data': 'This is my projects'})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(settings.DEFAULT_FROM_EMAIL,
              settings.EMAIL_BACKEND,
              settings.EMAIL_HOST,
              settings.EMAIL_HOST_PASSWORD,
              settings.EMAIL_HOST_USER,
              settings.EMAIL_PORT,
              settings.EMAIL_USE_SSL,
              settings.EMAIL_TIMEOUT,)
        send_mail(
            "Contact Form: Request for new update",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        obj = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        obj.save()
        return HttpResponseRedirect("/contact/")

    return render(request, 'contact.html', {'data': 'This is contact'})


def privacy(request):
    return render(request, 'privacy.html', {'data': 'This is my privacy'})


def terms(request):
    return render(request, 'terms.html', {'data': 'This is terms'})
