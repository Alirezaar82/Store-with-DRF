# Generated by Django 5.0.7 on 2024-07-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_productmodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='update'),
        ),
    ]
