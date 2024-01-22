from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def rrhh(request):
    return render(request, 'dashboard/rrhh/index.html')

def prd(request):
    return render(request, 'dashboard/prd/index.html')
