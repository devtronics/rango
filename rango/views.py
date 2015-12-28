from django.shortcuts import render
from rango_app.models import Category
from datetime import datetime
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
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if 'last_visit':
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True

    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

    context_dict['visits'] = visits

    response = render(request, 'index.html', context_dict)

    return response
