# Generated by Django 4.1.4 on 2023-04-28 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_usernews_email_usernews_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usernews',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]