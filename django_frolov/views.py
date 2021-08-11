from django.urls import reverse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
