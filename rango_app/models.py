from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # How do you think you might fix this error?
    # I changed it too false and still.
    # You must makemigrations after you change it.
    slug = models.SlugField(unique=False)

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    url = models.URLField()
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
