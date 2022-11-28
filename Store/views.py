from django.shortcuts import render
from .models import Watch

def home(request):
    watches = Watch.objects.all()
    return render(request, 'Store/home.html', {'watches' : watches})

def about(request):
    
    return render(request, 'Store/about.html')
