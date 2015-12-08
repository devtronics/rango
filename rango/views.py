from django.shortcuts import render
from rango_app.models import Category
# Create your views here.


def about(request):
    about_html = 'about.html'
    return render(request, about_html)

def contact(request):
    contact_html = 'contact.html'
    return render(request, contact_html)

def home(request):
    index_html = 'index.html'
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, index_html, context_dict)
