from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .models import *

# Register your models here.
# admin.site.register(Product)

admin.site.register(ProductImage)


class ImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


