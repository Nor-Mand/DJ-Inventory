from django.contrib import admin
from products.models import ProductTemplate, ProductCategory


@admin.register(ProductTemplate)
class ProductTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type', 'cost', 'price']


admin.site.register(ProductCategory)
