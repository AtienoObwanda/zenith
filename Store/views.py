from django.shortcuts import render, get_object_or_404
from .models import Watch, category, brand

def home(request):
    # watches = Watch.objects.all()
    # watches = Watch.objects.filter(is_active=True)
    watches = Watch.watch.all()
    categories = category.objects.all()
    return render(request, 'Store/home.html', {'watches' : watches, 'categories' : categories})

def about(request):
    
    return render(request, 'Store/about.html')


def watch_detail(request, slug):
    watch = get_object_or_404(Watch, slug=slug, in_stock = True)
    # brands = Watch.objects.filter(brand = watch.brand)
    return render(request, 'Store/watch.html', {'watch': watch})



def category_detail(request, category_slug):
    categories = category.objects.all()
    Category = get_object_or_404(category, slug=category_slug)
    watches = Watch.objects.filter(category=Category)
    return render(request, 'Store/category.html',{'Category': Category, 'watches': watches, 'categories' : categories})


def brand_detail(request, brand_slug):
    categories = category.objects.all()
    Brand = get_object_or_404(brand, slug=brand_slug)
    watches = Watch.objects.filter(brand = Brand)
    # categories = category.objects.filter(brand = Brand)
    return render(request, 'Store/brand.html', {'brand': brand, 'watches': watches,'categories' : categories})


