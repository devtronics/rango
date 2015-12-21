from django.shortcuts import render, render_to_response
from django.views.generic import View
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm
from rango.views import *
from rango_app.forms import PageForm
from django.template import RequestContext


def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__startswith=starts_with)
    else:
        cat_list = Category.objects.all()

    if max_results > 0:
        if (len(cat_list) > max_results):
            cat_list = cat_list[:max_results]

    for cat in cat_list:
        cat.url = encode_url(cat.name)

    return cat_list


def add_page(request, category_name_slug):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict['cat_list'] = cat_list

    category_name = str(category_name_slug)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            page = form.save(commit=False)

            # Retrieve the associated Category object so we can add it.
            try:
                cat = Category.objects.get(slug=category_name_slug)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response( 'add_page.html',
                                          context_dict,
                                          context)

            # Also, create a default value for the number of views.
            page.views = 0

            # With this, we can then save our new model instance.
            page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['category_name_slug']= str(category_name_slug)
    context_dict['category_name'] =  str(category_name)
    context_dict['form'] = form

    return render_to_response( 'add_page.html',
                               context_dict,
                               context)

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
    # Request our context
    context_dict = {}
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URL's don't handle spaces well, so we encode them as underscores.
    cat_list = get_category_list()
    context_dict['cat_list'] = cat_list

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name_slug'] = str(category.name)

        # Retrieve all of the associated pages.
        # Note teh filter returns >= 1 model instance
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context directory
        # Find the category with the given name.
        # Raises an exception if the category doesn't exist.
        # We also do a case insensitive match.

        # Well use this in the template to verify that the category exists
        context_dict['category'] = category
        if request.method == 'POST':
            query = request.POST.get('query')
            if query:
                query = query.strip()
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)

