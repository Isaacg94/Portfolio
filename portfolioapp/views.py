from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def landing(request):
    title = 'Home'
    return render(request, 'landing.html',{"title":title})