# Generated by Django 4.1.2 on 2022-11-22 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_category2_main_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category2',
            name='main_category',
        ),
    ]
