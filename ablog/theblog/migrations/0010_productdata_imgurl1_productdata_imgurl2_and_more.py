# Generated by Django 4.1.2 on 2022-10-27 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_productdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='imgURL1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='imgURL2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='imgURL3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
