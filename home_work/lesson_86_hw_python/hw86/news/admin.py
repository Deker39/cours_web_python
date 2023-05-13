from django.contrib import admin
from .models import *

admin.site.register(UserNews)
admin.site.register(CommentPost)
admin.site.register(ImageNewsPost)
admin.site.register(ParamsProject)


class ImageInline(admin.TabularInline):
    model = ImageNewsPost


@admin.register(NewsPost)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class PostCommentCountAdmin(admin.ModelAdmin):
    list_display = ('news', 'comment_count')


admin.site.register(PostCommentCount, PostCommentCountAdmin)