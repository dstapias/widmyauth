from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .auth0backend import getRole
from django.http import JsonResponse
import json
import requests


def widmy(request):
    return redirect('http://34.29.7.111:8000/')

def inicio(request):
    return render(request, 'inicio.html')

def ia(request):
    return redirect('http://34.29.7.111:8000/ia/')
