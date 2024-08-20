from django.contrib import admin
from .models import Product, ProductImage, User, Category, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(User)
admin.site.register(Order)


class ProductImageInlabe(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'price', 'category')
    inlines = [ProductImageInlabe, ]



