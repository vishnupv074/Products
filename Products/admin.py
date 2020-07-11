from django.contrib import admin
from . models import Category, Product, ProductImages, Features


# Register your models here.
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Product)
admin.site.register(Features)
