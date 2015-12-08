from django.shortcuts import render, render_to_response
from django.views.generic import View
from rango_app.models import Category
# Create your views here.

def rango_app_view(request):
    index_html = 'rango_app_index.html'
    return render(request, index_html)


class BootstrapView(View):
    template_name = 'bootstrap.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name)

def index(request):
    category_list = Category.objects.order_by('likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
