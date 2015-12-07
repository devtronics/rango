from django.shortcuts import render, render_to_response
from django.views.generic import View
# Create your views here.

def rango_app_view(request):
    index_html = 'rango_app_index.html'
    return render(request, index_html)


class BootstrapView(View):
    template_name = 'bootstrap.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name)
