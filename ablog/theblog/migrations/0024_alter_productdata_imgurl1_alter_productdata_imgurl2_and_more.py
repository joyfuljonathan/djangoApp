# Generated by Django 4.1.2 on 2023-01-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0023_alter_homeproductdata_imgurl1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdata',
            name='imgURL1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productdata',
            name='imgURL2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productdata',
            name='imgURL3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
