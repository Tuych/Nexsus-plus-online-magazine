from django.contrib import admin
from .models import Category, City, Product, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'parent')
    list_editable = ('parent', )
    list_display_links = ('id', 'name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user', 'city', 'address', 'price', 'discount', 'condition', 'status', 'created_date')
    list_editable = ('condition', 'price', 'discount')
    list_display_links = ('id', 'title')


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'detail_image')
    list_display_links = ('id', 'product')


admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
