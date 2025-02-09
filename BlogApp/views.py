from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.core.mail import send_mail
import datetime
import os
import json

# Get the base directory where manage.py is located
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to secrets.json
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")

with open(SECRETS_FILE) as file:
    secrets = json.load(file)

# Create your views here.

def index(request):
    return render(
        request,
        "BlogApp/index.html",
        {}
    )
    
def contact(request):
    form = forms.ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                send_mail(
                    subject='Contact Query from Usman Shahid Portfolio',
                    from_email=secrets["EMAIL_HOST_USER"],
                    message=f'name: {name}\nemail: {email}\nsubject: {subject}\nmessage: {message}',
                    recipient_list=[secrets["EMAIL_HOST_USER"], secrets["my_mail_1"], secrets["my_mail_2"]]
                )
                messages.success(
                    request,
                    'We have recieved your query and we will reply back to you soon!'
                )
                form.save()
                return redirect('/')
            except Exception as error:
                with open('logs.txt', 'w') as file:
                    file.write(f'Error Occured at contact view <{datetime.now()}>: {error}\n')
            form.save()
            messages.success(
                request,
                'Contact form submitted! We will soon reply to your query'
            )
            return redirect('/')
        else:
            messages.warning(
                request,
                f'Your form has errors\n{form.errors}'
            )
            # print(form.errors)
            return redirect('/')
    return redirect('/')

def custom_404(request, exception):
    messages.error(request, "Resource Not Found")
    return redirect("home")