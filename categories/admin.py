from django.contrib import admin

# Register your models here.

from .models import ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'name']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)
