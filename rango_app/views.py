from django.shortcuts import render

# Create your views here.

def rango_app_view(request):
    index_html = 'rango_app_index.html'
    return render(request, index_html)
