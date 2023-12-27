# Generated by Django 4.2.5 on 2023-12-27 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories_related', to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_related', to='myapp.category'),
        ),
    ]