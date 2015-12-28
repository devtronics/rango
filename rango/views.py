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
    context_dict = {'categories': category_list}

    visits = int(request.COOKIES.get('visits', '1'))

    reset_last_visit_time = False
    response = render(request, 'index.html', context_dict)

    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True

    else:
        reset_last_visit_time = True

        context_dict['visits'] = visits

        response = render(request, 'index.html', context_dict)

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    return response
