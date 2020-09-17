from django.shortcuts import render
from .models import Info
from django.conf import settings
from django.core.mail import send_mail


def send_message(request):
    info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request, 'contact.html', {'info': info})
