from django.contrib import admin

from . models import Category,product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug', 'description', 'cat_img')

admin.site.register(Category, CategoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'discription', 'price','images')

admin.site.register(product, productAdmin)