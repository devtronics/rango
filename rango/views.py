from django.shortcuts import render

# Create your views here.

def home(request):
    index_html = 'index.html'
    return render(request, index_html)

def about(request):
    about_html = 'about.html'
    return render(request, about_html)
