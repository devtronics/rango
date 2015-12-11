from django.shortcuts import render, render_to_response
from django.views.generic import View
from rango_app.models import Category, Page
# Create your views here.

def rango_app_view(request):
    index_html = 'rango_app_index.html'
    return render(request, index_html)


class BootstrapView(View):
    template_name = 'bootstrap.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name)

def category(request, category_name_slug):
    # Create a context dictioinary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        """ Can we find a category name slug with the given name?  If we can't, the .get() method raises a DoesNotExist exception.
        So the .get () method returns one model instance or raises an exception. """
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note teh filter returns >= 1 model instance
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context directory
        # Well use this in the template to verify that the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didnt find the specified category
        #  Dont do anython - the template displays the "no category" message for us
        pass
        # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

