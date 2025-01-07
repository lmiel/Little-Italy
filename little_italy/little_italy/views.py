import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    """Vista para la página de inicio."""
    return render(request, "little_italy/home.html")