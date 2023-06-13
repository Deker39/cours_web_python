from django.contrib import admin
from django.utils.html import format_html
from .models import *

admin.site.register(ShopUser)
admin.site.register(ProductKey)
admin.site.register(CommentProduct)
admin.site.register(Order)
admin.site.register(OrdersList)
admin.site.register(ProductsDay)


class ImageInline(admin.TabularInline):
    model = ProductPhoto
    extra = 0
    readonly_fields = ['display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)


class SystemRequirementInline(admin.StackedInline):
    model = ProductSystemRequirement
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, SystemRequirementInline]
    list_display = ("title", "display_main_image")
    readonly_fields = ['display_main_image']
    prepopulated_fields = {"slug": ("title",)}

    def display_main_image(self, obj):
        return format_html('<img src="{}" width="150" height="200" />', obj.main_image.url)

    display_main_image.short_description = 'Main Image'


class CatalogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(CatalogProduct, CatalogAdmin)
