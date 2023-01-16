from django.db import models
from django.urls import reverse


# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='content')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='time create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='time update')
    is_published = models.BooleanField(default=True, verbose_name='is published')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category')

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return  reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Famous women'
        verbose_name_plural = 'Famous women'
        ordering = ['time_create','title']

class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    url_name = models.CharField(max_length=255,null=True, verbose_name='url name')

    def __str(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name='category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

