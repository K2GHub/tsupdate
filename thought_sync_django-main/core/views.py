from django.shortcuts import render

# Create your views here.

# your_app/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['willijos@lafayette.edu']

    try:
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse('Email sent successfully.')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {str(e)}')
