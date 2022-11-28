from django.shortcuts import render, get_object_or_404
from .models import Watch, category

def home(request):
    watches = Watch.objects.all()
    categories = category.objects.all()
    return render(request, 'Store/home.html', {'watches' : watches, 'categories' : categories})

def about(request):
    
    return render(request, 'Store/about.html')


def watch_detail(request, slug):
    watch = get_object_or_404(Watch, slug=slug, in_stock = True)
    return render(request, 'Store/watch.html', {'watch': watch})