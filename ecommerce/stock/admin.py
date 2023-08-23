from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description','stok',)
    search_fields = ('name','short_description')
    list_filter = ('discount_until','stok',)
    date_hierarchy = 'discount_until'

admin.site.register(Product, ProductAdmin)