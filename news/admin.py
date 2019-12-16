from django.contrib import admin

from .models import News
# Register your models here.
list_display = ('id', 'title', 'is_published', 'chef')

list_display_links = ('id', 'title')

list_filter = ('chef',)

list_editable = ('is_published',)

search_fields = ('title', 'description')

list_per_page = 25


admin.site.register(News)