# Generated by Django 4.2.5 on 2023-12-27 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_product_image_url_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
