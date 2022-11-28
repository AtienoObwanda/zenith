from django.shortcuts import render, get_object_or_404
from .models import Watch, category, brand

def home(request):
    watches = Watch.objects.all()
    categories = category.objects.all()
    return render(request, 'Store/home.html', {'watches' : watches, 'categories' : categories})

def about(request):
    
    return render(request, 'Store/about.html')


def watch_detail(request, slug):
    watch = get_object_or_404(Watch, slug=slug, in_stock = True)
    return render(request, 'Store/watch.html', {'watch': watch})


def cart_page(request):
    return render(request, 'Store/cart.html')


def category_detail(request, category_slug):
    category = get_object_or_404(category, slug = category_slug)
    watches = Watch.objects.filter(category = category)
    return render(request, 'Store/category.html',{'category': category, 'watches': watches})


def brand_detail(request, brand_slug):
    brand = get_object_or_404(brand, slug=brand_slug)
    watches = Watch.objects.filter(category = category)
    return render(request, 'Store/brand.html', {'brand': brand, 'watches': watches})


