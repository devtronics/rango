from django.shortcuts import render
from rango_app.models import Category, Page
from datetime import datetime
from rango_app.views import *

# Create your views here.
def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def about(request):
    about_html = 'about.html'
    return render(request, about_html)

def contact(request):
    contact_html = 'contact.html'
    return render(request, contact_html)

def home(request):
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]

    for category in category_list:
        category.url = encode_url(category.name)

    context_dict = {'categories': category_list}

    cat_list = get_category_list()

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list


    if request.session.get('last_visit'):

        last_visit_time = request.session.get('last_visit')

        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            visits = visits + 1

    else:

        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1


    return render_to_response('index.html', context_dict, context)
