# Generated by Django 3.2.11 on 2022-01-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_prd_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='prd_category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='prd_created',
        ),
        migrations.RemoveField(
            model_name='products',
            name='prd_discount_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='prd_image',
        ),
        migrations.RemoveField(
            model_name='products',
            name='prd_updated',
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]