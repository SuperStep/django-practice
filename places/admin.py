from django.contrib import admin
from .models import Category, Place

admin.AdminSite.site_header = 'Администрация сайта'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    model = Category
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    model = Place
    extra = 1

admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)