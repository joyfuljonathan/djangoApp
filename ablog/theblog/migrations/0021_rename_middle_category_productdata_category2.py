# Generated by Django 4.1.2 on 2022-11-22 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0020_category2_main_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdata',
            old_name='middle_category',
            new_name='category2',
        ),
    ]
