from django.shortcuts import render, get_object_or_404
from .models import Platforms

# app_name = 'readquestions'
# Create your views here.

def home(request):
    platforms = Platforms.objects.all()
    return render(request, 'readquestions/home.html', {"platforms": platforms})

def details(request, platformId):
    platform = get_object_or_404(Platforms, pk=platformId)
    return render(request, 'readquestions/detail.html', {"platform":platform})
