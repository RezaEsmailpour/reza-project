from django.contrib import admin

from .models import Food
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'chef')

    list_display_links = ('id', 'title')

    list_filter = ('chef',)

    list_editable = ('is_published',)

    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

    list_per_page = 25


admin.site.register(Food)