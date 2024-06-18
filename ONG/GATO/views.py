from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html');

def login(request):
    return render(request,'login.html');

def listadegatos(request):
    return render(request,'listadegatos.html');

def listadeperros(request):
    return render(request,'listadeperros.html');

def tobi(request):
    return render(request,'tobi.html');

def max(request):
    return render(request,'Max.html');