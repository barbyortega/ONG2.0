from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={}
    return render(request,'index.html',context)

def admin(request):
    context={}
    return render(request,'html/admin.html',context)



