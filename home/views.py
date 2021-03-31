from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, auth
import emoji



# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, desc=desc, date=datetime.today())
        contact.save()
        print("sarthak")
        messages.success(request, "Your message has been sent!!! THANK YOU \U0001F603")
    return render(request, 'index.html')

