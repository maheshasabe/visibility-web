from django.shortcuts import render, get_object_or_404
from .models import Platforms

# app_name = 'readquestions'
# Create your views here.

def home(request):
    platforms = Platforms.objects.all()
    return render(request, 'readquestions/index.html', {"platforms": platforms})

def details(request, platformId):
    platform = get_object_or_404(Platforms, pk=platformId)
    return render(request, 'readquestions/detail.html', {"platform":platform})

def about(request):
    return render(request, 'readquestions/about.html')

def courses(request):
    return render(request, 'readquestions/courses.html')

def faq(request):
    return render(request, 'readquestions/faq.html')

def contact(request):
    return render(request, 'readquestions/contact.html')

def blog(request):
    return render(request, 'readquestions/blog.html')