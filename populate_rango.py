import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango.settings')

import django
django.setup()

from range.models import Category, Page

def populate():
    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/"

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorial/python/")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/"

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.or/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask"
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()

