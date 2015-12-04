from django.shortcuts import render

# Create your views here.

def home(request):
    index_html = 'index.html'
    return render(request, index_html)

