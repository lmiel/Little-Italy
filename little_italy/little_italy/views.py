from django.shortcuts import render


def home(request):
    """Vista para la página de inicio."""
    return render(request, "little_italy/home.html")
