from django.shortcuts import render, render_to_response
from django.views.generic import View
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm
from rango.views import *
from rango_app.forms import PageForm

# Create your views here.
def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'rango_app/add_page.html', context_dict)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return home(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})

class BootstrapView(View):
    template_name = 'bootstrap.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name)

def category(request, category_name_slug):
    context_dict = {}

    try:
        """ Can we find a category name slug with the given name?  If we can't, the .get() method raises a DoesNotExist exception.
        So the .get () method returns one model instance or raises an exception. """
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name_slug'] = category.name

        # Retrieve all of the associated pages.
        # Note teh filter returns >= 1 model instance
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context directory
        # Well use this in the template to verify that the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)



