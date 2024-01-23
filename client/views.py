from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')


def rrhh(request):
    return render(request, 'dashboard/rrhh/index.html')

def ingreso_personal(request):
    return render(request, 'dashboard/rrhh/ingreso_personal.html')


def liquidaciones(request):
    return render(request, 'dashboard/rrhh/liquidaciones.html')


def prd(request):
    return render(request, 'dashboard/prd/index.html')
