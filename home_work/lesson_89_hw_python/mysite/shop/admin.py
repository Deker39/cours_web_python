from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CatalogProduct)
# admin.site.register(ProductSystemRequirement)
admin.site.register(ProductKey)
admin.site.register(CommentProduct)
admin.site.register(Order)
admin.site.register(OrdersList)
admin.site.register(ProductsDay)


class ImageInline(admin.TabularInline):
    model = ProductPhoto
    extra = 0


class SystemRequirementInline(admin.StackedInline):
    model = ProductSystemRequirement
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, SystemRequirementInline]

