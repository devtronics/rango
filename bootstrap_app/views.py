from django.shortcuts import render
from django.views.generic import CreateView


# Create your views here.


class BootstrapView(CreateView):

    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
