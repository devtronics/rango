from django.contrib import admin
from rango_app.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    # 0, title 1, category, 2, url
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
