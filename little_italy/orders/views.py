import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# Usar la API Key desde settings
SPOONACULAR_API_KEY = settings.SPOONACULAR_API_KEY
# Create your views here.

def home(request):
    return render(request, 'orders/home.html')

