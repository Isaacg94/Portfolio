from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewsLetterForm
from .email import send_welcome_email
from .models import *

# Create your views here.
def landing(request):
    title = 'Home'

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('landing')
    else:
        form = NewsLetterForm()
    
    return render(request, 'landing.html',{"title":title,"letterForm":form})