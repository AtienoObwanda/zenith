from django.shortcuts import render

def home(request):
    
    return render(request, 'Store/home.html')

def about(request):
    
    return render(request, 'Store/about.html')