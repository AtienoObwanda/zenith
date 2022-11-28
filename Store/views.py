from django.shortcuts import render
from .models import Watch, category

def home(request):
    watches = Watch.objects.all()
    categories = category.objects.all()
    return render(request, 'Store/home.html', {'watches' : watches, 'categories' : categories})

def about(request):
    
    return render(request, 'Store/about.html')
