from django.shortcuts import render
from .logic import autenticacion_logic as al
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def autenticacion_buscar(request):
    return 1