from django.contrib import admin

from .models import Chef
# Register your models here.

class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'work_date')

    list_display_links = ('id', 'name')

    search_fields = ('name',)

    list_per_page = 25

admin.site.register(Chef)