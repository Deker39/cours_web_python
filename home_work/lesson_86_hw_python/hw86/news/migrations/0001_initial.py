# Generated by Django 4.1.4 on 2023-04-23 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParamsProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(max_length=100)),
                ('color_text', models.CharField(max_length=100)),
                ('size_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firs_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('ban', models.BooleanField()),
                ('ban_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageNewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/')),
                ('newspost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='news.newspost')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth', to='news.usernews')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='news.newspost')),
            ],
        ),
    ]