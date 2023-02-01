# from typing_extensions import Concatenate
from django.contrib import admin
from .models import Post, Category, Product, ProductData, Category2, HomeProductData
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductData)
admin.site.register(Category2)
admin.site.register(HomeProductData)

